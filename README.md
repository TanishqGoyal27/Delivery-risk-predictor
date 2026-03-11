# Delivery Risk Predictor

## Overview

This project predicts whether an e-commerce delivery will be **On-Time**, **At-Risk**, or **Delayed** using machine learning.
The model analyzes logistics and operational features such as shipment distance, warehouse processing time, seller reliability, traffic conditions, and weather indicators.

An interactive web application was built using Streamlit so users can input delivery details and instantly get a prediction.

---

## Features

* Data integration from multiple logistics datasets
* Feature engineering including shipment distance and seller performance metrics
* Handling class imbalance using SMOTE
* Training and comparison of multiple machine learning models
* Model evaluation using Accuracy, Precision, Recall, and F1 Score
* Visualization using confusion matrix and ROC curves
* Interactive prediction interface using Streamlit

---

## Machine Learning Models Used

* Random Forest
* Logistic Regression
* Decision Tree
* K-Nearest Neighbors (KNN)

Random Forest achieved the best performance and was selected as the final model.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn

---

## Project Structure

```
delivery-risk-predictor
│
├── app.py                     # Streamlit web application
├── delivery_risk_model.pkl   # Trained machine learning model
├── requirements.txt          # Python dependencies
│
├── data/                     # Dataset files
│
└── notebook/
    └── code.ipynb            # Model development notebook
```

---

## Run the Project Locally

### 1. Clone the repository

```
git clone https://github.com/TanishqGoyal27/Delivery-risk-predictor.git
cd Delivery-risk-predictor
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## Example Prediction Inputs

The model takes the following inputs:

* Order Volume
* Warehouse Processing Time
* Shipment Distance
* Seller On-Time Rate
* Delivery Time (days)
* Traffic Condition
* Weather Indicator

Based on these inputs, the model predicts whether the delivery is likely to be **On-Time**, **At-Risk**, or **Delayed**.

---

## Future Improvements

* Deploy the application publicly using Streamlit Cloud
* Add more advanced models such as XGBoost
* Integrate real-time logistics data
* Improve feature engineering with additional delivery metrics

---

## Author

Tanishq Goyal
B.Tech Computer Engineering
Thapar Institute of Engineering and Technology
