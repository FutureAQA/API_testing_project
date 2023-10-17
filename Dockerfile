FROM python:3.11-alpine
LABEL authors="Denis"

RUN python3 -m pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python -m pytest -sv /app/tests/