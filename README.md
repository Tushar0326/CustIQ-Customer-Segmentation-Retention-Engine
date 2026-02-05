🚀 CustIQ – AI-Powered Customer Intelligence & Retention Platform

CustIQ is an end-to-end AI-driven customer analytics system that helps businesses understand customer behavior, predict churn risk, and recommend ROI-optimized retention strategies.

It transforms raw transactional data into actionable business intelligence using machine learning, explainable AI, and real-time prediction services.

🌟 Key Features
📊 Customer Analytics

RFM-based customer segmentation

Behavioral clustering using K-Means

Customer lifetime value approximation

🤖 Machine Learning

Churn prediction using Random Forest

Supervised + Unsupervised ML pipeline

Feature scaling and preprocessing pipeline

🔍 Explainable AI

SHAP-based churn driver explanation

Global and customer-level interpretability

💰 Retention Intelligence

Risk-based customer targeting

ROI-driven retention recommendation engine

Marketing budget optimization

🌐 Production Deployment

FastAPI real-time prediction API

Streamlit interactive dashboard

Docker containerized deployment

Cloud-ready architecture

🧠 Business Problem

Customer churn significantly impacts revenue and customer lifetime value.
Most companies lack actionable insights to:

Identify high-value customers

Predict churn risk

Optimize retention spending

Understand behavioral churn drivers

CustIQ solves this by combining data analytics, AI, and business decision modeling.

🏗 System Architecture
Transaction Data
      ↓
Data Cleaning & Feature Engineering
      ↓
RFM Segmentation
      ↓
ML Clustering & Churn Prediction
      ↓
Explainable AI (SHAP)
      ↓
ROI-Based Retention Engine
      ↓
FastAPI Prediction Service
      ↓
Streamlit Business Dashboard

🛠 Tech Stack
Data & ML

Python

Pandas, NumPy

Scikit-learn

SHAP

Backend

FastAPI

Pydantic

Joblib

Frontend

Streamlit

Requests

Deployment

Docker

Render (Cloud Hosting)

📁 Project Structure
CustIQ/
│
├── app/                    # FastAPI backend
├── dashboard/              # Streamlit UI
├── data/                   # Raw & processed datasets
├── models/                 # Trained ML models
├── notebooks/              # ML development notebooks
├── outputs/                # Reports & predictions
├── Dockerfile
├── requirements.txt
└── README.md

⚙ Installation & Setup
Clone Repository
git clone https://github.com/Tushar0326/CustIQ-Customer-Segmentation-Retention-Engine.git
cd CustIQ

Install Dependencies
pip install -r requirements.txt

▶ Running FastAPI Server
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

📊 Running Streamlit Dashboard
streamlit run dashboard/app.py

🐳 Docker Deployment
Build Image
docker build -t custiq-api .

Run Container
docker run -p 8000:8000 custiq-api

☁ Cloud Deployment

CustIQ backend is deployable on:

Render

AWS ECS

Google Cloud Run

Azure Container Apps

📈 Machine Learning Pipeline
1️⃣ RFM Segmentation

Recency

Frequency

Monetary value

2️⃣ Customer Clustering

K-Means segmentation

Behavioral grouping

3️⃣ Churn Prediction

Random Forest classifier

Probability-based churn scoring

4️⃣ Explainable AI

SHAP feature attribution

Customer-level churn reasoning

5️⃣ Retention Engine

Risk classification

ROI-based intervention planning

📊 Example API Request
Endpoint
POST /predict

Input
{
  "Recency": 120,
  "Frequency": 2,
  "Monetary": 350,
  "Cluster": 1
}

Output
{
  "Churn Prediction": 1,
  "Churn Probability": 0.76
}

📌 Business Impact

CustIQ helps organizations:

Improve customer retention

Reduce marketing waste

Increase customer lifetime value

Gain explainable customer intelligence

🔮 Future Enhancements

Real-time streaming data integration

Automated ML retraining pipeline

SaaS multi-tenant dashboard

Feature store integration

Multi-model ensemble churn system
