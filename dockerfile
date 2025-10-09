# Sử dụng Python base image
FROM python:3.10-slim

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
# copy code
COPY . .

# App nghe 5000
EXPOSE 5000

# Chạy bằng Gunicorn 
CMD ["gunicorn","-b","0.0.0.0:5000","app:app","--workers","2","--timeout","60"]