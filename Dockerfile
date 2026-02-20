FROM python:3.10-slim

WORKDIR /app

# Install required system dependencies for TensorFlow
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "gunicorn main:app -k uvicorn.workers.UvicornWorker --workers 1 --threads 1 --timeout 120 --preload --bind 0.0.0.0:$PORT"]
