# Use official Python image
FROM python:3.10-slim

# Prevent Python .pyc and enable clean logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy requirements FIRST (for caching)
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL frontend files
COPY . /app

# Expose Render port
EXPOSE 10000

# Start Streamlit on required Render port
CMD ["streamlit", "run", "app.py", "--server.port=10000", "--server.address=0.0.0.0"]
