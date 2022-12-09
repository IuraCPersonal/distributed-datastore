# Install the base requirements for the app.
# This stage is to support development.
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Dev-ready container
COPY . .
CMD ["python", "run.py"]

# CMD ["gunicorn", "--bind", "0.0.0.0", "--workers", "1", "run:app"]