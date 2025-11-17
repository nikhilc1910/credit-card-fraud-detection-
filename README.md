# 🚀 Credit Card Fraud Detection System  
**Built with FastAPI, Streamlit, Machine Learning & Docker**

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-darkgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://www.docker.com/)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)

---

## 🌟 Project Overview  
This project is an **end-to-end Machine Learning system** designed to detect **fraudulent credit card transactions** using a Random Forest model.

### The system includes:
- ✔ **FastAPI backend** (ML model API)
- ✔ **Streamlit frontend** (User interface)
- ✔ **Docker containerization**
- ✔ **Deployment on Render (API + Frontend)**

---

## 🌐 Live Deployment  

### 🔵 **Frontend (Streamlit UI)**  
👉 https://frontend-pd73.onrender.com  

### 🟢 **Backend (FastAPI API)**  
👉 https://credit-card-fraud-detection-4mjn.onrender.com/docs  

---

## 🧠 Problem Statement  
Credit card fraud causes billions in losses globally.  
This system predicts whether a transaction is **fraudulent** or **legitimate** based on:

- Hours since dataset start  
- Transaction type  
- Transaction amount  
- Sender & receiver balances  
- Fraud flag indicators  

The dataset used is the **PaySim simulator dataset** (synthetic, privacy-safe).

📊 Dataset: https://www.kaggle.com/datasets/ealaxi/paysim1

---

## ⚙️ Tech Stack  
| Component | Technology |
|----------|------------|
| **Model** | Random Forest Classifier |
| **Backend** | FastAPI + Uvicorn |
| **Frontend** | Streamlit |
| **Containerization** | Docker |
| **Deployment** | Render Cloud |

---

## 🧪 Model Performance  
Two models were compared:

| Model | Accuracy | F1 Score |
|-------|----------|----------|
| Logistic Regression | Moderate | Low |
| **Random Forest (Selected)** | **0.99 Accuracy** | **0.86 F1 Score** |

The Random Forest model performed the best and was exported as `credit_fraud.pkl`.

---

## 📁 Project Structure  
