#!/bin/bash

echo "Starting FastAPI application..."
cd /home/site/wwwroot

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python -c "from app.db import init_db; init_db()"

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 --workers 4 --worker-class uvicorn.workers.UvicornWorker app.main:app
