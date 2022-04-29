# app/auth/auth_handler.py
from app.database.dboperation import connect_db, close_db_conn

import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 300  # 5 minutes validity
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    conn = connect_db()
    cur = conn.cursor()
    query = "select * from token"
    cur.execute(query)
    total_rec = len(cur.fetchall())
    query = "insert into token values("+str(total_rec+1)+",'"+payload["user_id"] + \
            "','"+token+"',"+str(payload["expires"])+")"
    cur.execute(query)
    conn.commit()
    close_db_conn(conn)
    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        token = decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        print(e)
        token = {}
    return token
