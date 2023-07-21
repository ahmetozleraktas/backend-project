FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt ./
# Path: /app
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x *.sh