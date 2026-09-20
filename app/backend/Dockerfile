FROM python:3.14-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application and trained model into container
COPY app.py .
COPY superkart_model.joblib .

EXPOSE 7860

CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:superkart_api"]
