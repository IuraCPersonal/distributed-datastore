# Install the base requirements for the app.
# This stage is to support development.
FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Dev-ready container
COPY . .
CMD ["python", "-u", "run.py"]
