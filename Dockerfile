# Use a lightweight Python image
FROM python:3-slim

# Set the working directory inside the container
WORKDIR /app

# Expose the port Flask runs on
EXPOSE 5002

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install required system dependencies for MySQL client
RUN apt update && apt install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker caching
COPY requirements.txt ./

# Install Python dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Create a non-root user and set permissions
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Start the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "--workers", "4", "adoption_site:app"]
