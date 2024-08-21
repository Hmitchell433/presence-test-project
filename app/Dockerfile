FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app:/app/app_cmd"

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "cmd/server/main.py"]
