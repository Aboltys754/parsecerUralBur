FROM python:3.12-alpine3.20

WORKDIR /src

RUN wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chrome-linux64.zip

RUN unzip chrome-linux64.zip

RUN wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chromedriver-linux64.zip

RUN unzip chromedriver-linux64.zip

COPY ./requirements.txt /src/requirements.txt

COPY ./chromedriver-linux64 /src/chromedriver-linux64

COPY ./chromedriver-linux64 /src/chrome-linux64

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]