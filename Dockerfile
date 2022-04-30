FROM python:3.9

WORKDIR /mathwebservice

COPY requirements.txt /mathwebservice/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /mathwebservice/requirements.txt

COPY ./app /mathwebservice/app

COPY .env /mathwebservice/.env

COPY ./tests /mathwebservice/tests

copy users.db /mathwebservice

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
