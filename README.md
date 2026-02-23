Customer Lifetime Value (CLV) Prediction using MySQL & Python

📌 Project Overview

This project focuses on building a Customer Lifetime Value (CLV) prediction model using historical transaction data. The objective is to extract data from a MySQL database, perform data cleaning and feature engineering using RFM (Recency, Frequency, Monetary) analysis, and train a regression model to estimate CLV. The results are evaluated using standard performance metrics and interpreted for business decision-making.

🛠️ Technologies Used

Python

Pandas, NumPy

Scikit-learn

MySQL

SQLAlchemy

📂 Project Structure
CLV_Project/
│
├── clv_prediction.py        # MySQL ETL + data cleaning + model training
├── README.md                # Project documentation
└── (Optional) screenshots/  # Output screenshots (if added)

🔄 ETL Process (MySQL → Python)

Transactional data is stored in a MySQL database.

Data is extracted using SQLAlchemy and SQL queries.

The extracted data is loaded into a Pandas DataFrame.

Data cleaning is performed to handle:

Invalid or missing dates

Invalid transaction amounts

⚙️ Feature Engineering (RFM Analysis)

For each customer, the following features are engineered:

Recency: Days since the most recent transaction

Frequency: Number of transactions

Monetary: Total amount spent

The CLV is approximated using the historical monetary value.

🤖 Model Development

Model Used: Random Forest Regressor

Input Features: Recency, Frequency, Monetary

Target Variable: Customer Lifetime Value (CLV)

The dataset is split into training and testing sets, and the model is trained to predict CLV.

📊 Model Performance

RMSE: 256.30

R² Score: 0.27

The RMSE indicates reasonable prediction accuracy given the small dataset size. The positive R² score shows that the model performs better than a baseline mean predictor.

📈 Feature Importance Insights

Monetary Value: Most influential feature (~68%)

Recency: Second most important feature (~29%)

Frequency: Lower impact due to similar purchase counts across customers

💡 Business Implications

High-spending and recently active customers should be prioritized for retention and loyalty programs.

Customers with high past spending but low recent activity can be targeted using reactivation campaigns.

Marketing resources can be optimized by focusing on customers with higher predicted CLV.

▶️ How to Run the Project

Ensure MySQL is running and the database/table are set up.

Update MySQL credentials in clv_prediction.py.

Install dependencies:

pip install pandas numpy scikit-learn sqlalchemy mysql-connector-python


Run the script:

python clv_prediction.py

✅ Conclusion

This project demonstrates an end-to-end data analytics and machine learning workflow, from MySQL-based ETL to CLV prediction and business insight generation. It highlights how transactional data can be transformed into actionable intelligence to support customer-centric business strategies.
This repository focuses on conceptual clarity, structured thinking, and practical approaches, rather than only code, to reflect real interview and job expectations.
