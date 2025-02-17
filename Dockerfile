FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y dovecot-common dovecot-core

COPY src/ ./src/

CMD ["python", "src/main.py"]