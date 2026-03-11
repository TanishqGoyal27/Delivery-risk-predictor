# Delivery Risk Predictor

## Live Demo

Access the deployed application here:

**[https://delivery-risk-predictor.streamlit.app](https://delivery-risk-predictor.streamlit.app)**

This interactive web application predicts whether an e-commerce delivery will be **On-Time**, **At-Risk**, or **Delayed** based on operational and logistics features.

---

# Overview

Efficient logistics management is critical for e-commerce platforms. Delivery delays can negatively impact customer satisfaction and operational efficiency.

This project uses **machine learning** to predict delivery risk using key logistics indicators such as:

* shipment distance
* warehouse processing time
* seller reliability
* traffic conditions
* weather conditions

An interactive **Streamlit dashboard** allows users to input delivery parameters and receive real-time predictions.

---

# Key Features

* Machine learning pipeline for delivery risk prediction
* Handling class imbalance using **SMOTE**
* Training and evaluation of multiple ML models
* Selection of **Random Forest** as the best-performing model
* Interactive web interface built with **Streamlit**
* Real-time predictions with confidence estimation
* Visualizations for model evaluation

---

# Machine Learning Workflow

The project follows a complete ML pipeline:

```
Data Collection
      ↓
Data Cleaning & Feature Engineering
      ↓
Handling Class Imbalance (SMOTE)
      ↓
Model Training & Evaluation
      ↓
Model Selection (Random Forest)
      ↓
Model Deployment (Streamlit App)
```

---

# Machine Learning Models Evaluated

The following models were trained and compared:

* Random Forest
* Logistic Regression
* Decision Tree
* K-Nearest Neighbors (KNN)

Random Forest produced the **highest accuracy and best overall performance**, so it was selected as the final model.

---

# Technology Stack

**Programming Language**

* Python

**Data Processing**

* Pandas
* NumPy

**Machine Learning**

* Scikit-learn
* Imbalanced-learn (SMOTE)

**Visualization**

* Matplotlib
* Seaborn

**Web Application**

* Streamlit

---

# Project Structure

```
delivery-risk-predictor
│
├── app.py
│   Streamlit application for delivery risk prediction
│
├── delivery_risk_model.pkl
│   Trained Random Forest model
│
├── requirements.txt
│   Project dependencies
│
├── data/
│   Dataset files used for training
│
└── notebook/
    └── code.ipynb
       Model training and experimentation notebook
```

---

# Running the Project Locally

### Clone the Repository

```
git clone https://github.com/TanishqGoyal27/Delivery-risk-predictor.git
cd Delivery-risk-predictor
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run the Application

```
streamlit run app.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

# Model Inputs

The prediction model uses the following features:

* Order Volume
* Warehouse Processing Time (hours)
* Shipment Distance (km)
* Seller On-Time Rate
* Delivery Time (days)
* Traffic Condition
* Weather Condition

Based on these parameters, the model predicts whether a delivery will be:

* **On-Time**
* **At-Risk**
* **Delayed**

---

# Example Use Case

A logistics manager can use this tool to:

* estimate delivery risk before dispatch
* identify potential delays
* optimize warehouse processing
* improve delivery reliability

---

# Future Improvements

Potential enhancements include:

* Integration with real-time logistics data
* Addition of advanced models such as **XGBoost**
* Explainable AI techniques (feature importance)
* Improved dashboard visualizations
* API-based deployment for enterprise systems

---

# Author

**Tanishq Goyal**

B.Tech Computer Engineering
Thapar Institute of Engineering and Technology

---

# License

This project is for educational and research purposes.

---
