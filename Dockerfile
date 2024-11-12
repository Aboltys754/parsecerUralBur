FROM python:3.12-alpine3.20

WORKDIR /src

COPY ./ /src/

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]