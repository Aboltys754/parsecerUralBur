FROM python:3.12-slim

WORKDIR /src

COPY ./main.py /src/main.py

COPY ./parcer.py /src/parcer.py

COPY ./requirements.txt /src/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

RUN apt-get update && apt-get install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm ./google-chrome-stable_current_amd64.deb

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]