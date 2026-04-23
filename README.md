# 🚀 End-to-End Telecom Churn Prediction System 🚀

Interface --
<img width="1536" height="1024" alt="ChatGPT Image Apr 23, 2026, 06_13_14 PM" src="https://github.com/user-attachments/assets/69e1bc60-691f-44ea-89f1-a3366c03828c" />


## 📌 Overview
This project is a **production-oriented machine learning system** designed to predict customer churn in the telecom industry. It goes beyond basic modeling by implementing a **modular ML pipeline, model evaluation framework, and an interactive deployment layer**.
The system enables businesses to **identify high-risk customers in real time**, allowing targeted retention strategies and improved customer lifetime value.

---

## 🎯 Business Objective
Customer acquisition is significantly more expensive than retention. This system addresses:
* 🔍 **Churn Prediction** — Identify customers likely to leave
* 📊 **Risk Scoring** — Estimate churn probability
* 🎯 **Actionable Insights** — Support retention campaigns

---

## 🧠 Machine Learning Pipeline
### 🔹 Data Processing
* Missing value imputation (median / mode strategy)
* Outlier detection & capping (IQR-based)
* Feature encoding:
* OneHotEncoding (categorical variables)
* Feature scaling:
* StandardScaler (numerical features)

---

### 🔹 Pipeline Architecture
The model is built using a **Scikit-learn Pipeline** with a `ColumnTransformer`:
* Numerical → Scaling
* Categorical → Encoding
* Final estimator → XGBoost
This ensures:
* No data leakage
* Consistent preprocessing during inference
* Production-ready transformation

---

### 🔹 Models Evaluated
| Model               | Accuracy | ROC-AUC  |
| ------------------- | -------- | -------- |
| Logistic Regression | 0.80     | 0.84     |
| Random Forest       | 0.84     | 0.88     |
| ✅ XGBoost           | **0.86** | **0.90** |

**Final Model:** XGBoost (best generalization performance)

---

### 🔹 Evaluation Metrics

* Accuracy
* Precision / Recall
* F1 Score
* ROC-AUC

---

## 🏗️ Project Structure

```
end-to-end-churn-prediction-system/
│
├── data/                  # Raw & processed datasets
├── notebooks/             # EDA & experimentation
├── src/                   # Core ML pipeline
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│
├── models/                # Saved trained model
│   └── churn_model.pkl
│
├── api/                   # FastAPI backend (optional)
│   └── app.py
│
├── dashboard/             # Streamlit UI
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Python** — Core language
* **Pandas / NumPy** — Data processing
* **Scikit-learn** — ML pipeline & evaluation
* **XGBoost** — Final model
* **Streamlit** — Interactive UI
* **FastAPI** — API layer (optional)
* **Joblib** — Model serialization

---

## 🚀 Features

* End-to-end ML pipeline
* Real-time churn prediction
* Interactive dashboard UI
* Probability-based risk scoring
* Modular and scalable architecture

---

## ▶️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/yourusername/end-to-end-churn-prediction-system.git
cd end-to-end-churn-prediction-system

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run dashboard/app.py
```

---

## 🌐 Deployment

### 🔗 Live Demo

(Add your deployed link here)

```
https://your-streamlit-app-url
```

---

### 🔌 API Endpoint (Optional)

```bash
POST /predict
```

#### Example Request:

```json
{
  "tenure": 12,
  "monthly_charges": 70.5,
  "contract": "Month-to-month"
}
```

#### Example Response:

```json
{
  "churn": true,
  "probability": 0.87
}
```

---

## 📊 Dashboard Capabilities

* User input interface
* Real-time prediction
* Churn probability visualization
* Business-friendly outputs

---

## ⚠️ Known Limitations

* Model serialization uses `joblib/pickle`, which may cause compatibility issues across Python or library versions
* Recommended to retrain model in the deployment environment for stability

---

## 🔮 Future Enhancements

* 🔍 Model explainability (SHAP)
* ☁️ Cloud deployment (AWS / Render)
* 🔄 CI/CD pipeline integration
* 📡 Real-time data ingestion
* 📉 Model monitoring & drift detection

---

## 📈 Key Learnings

* Designing production-ready ML pipelines
* Feature engineering for tabular datasets
* Model evaluation & selection strategies
* Deploying ML models with UI/API
* Structuring scalable ML systems

---

## 🤝 Contributing
Contributions are welcome.
Feel free to open issues or submit pull requests.

---

## 👤 Author
**Saurav Pawar**
Aspiring Data Scientist | Machine Learning Enthusiast

---

## ⭐ Support
If you found this project useful, consider giving it a ⭐
It helps increase visibility and supports further development.
