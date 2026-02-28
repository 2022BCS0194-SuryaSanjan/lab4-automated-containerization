FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ scripts/
COPY dataset/ dataset/

# Generate model during build
RUN python scripts/train.py

EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "scripts.app:app", "--host", "0.0.0.0", "--port", "8000"]
