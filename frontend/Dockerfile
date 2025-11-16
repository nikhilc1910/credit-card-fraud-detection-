# frontend/Dockerfile

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

# Streamlit must bind to Render's dynamic port
CMD streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT
