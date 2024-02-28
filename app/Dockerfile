# Smaller Alpine image
FROM python:3.11-alpine

WORKDIR /app

# Only copying needed files
COPY requirements.txt ./

RUN apk add libmagic

# Multiple commands in a single RUN invocation
RUN  pip install --upgrade pip && pip install -r requirements.txt && rm -rf ~/.cache/pip

COPY . . 