FROM python:3.12 

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src

RUN wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chrome-linux64.zip

RUN unzip chrome-linux64.zip

RUN wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.91/linux64/chromedriver-linux64.zip

RUN unzip chromedriver-linux64.zip

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]