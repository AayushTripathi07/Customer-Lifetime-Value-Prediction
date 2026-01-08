import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

engine = create_engine(
    "mysql+mysqlconnector://root:Aayush07%40@localhost:3306/clv_db"
)

query = """
SELECT customer_id, order_date, order_amount
FROM sales_transactions
"""

df = pd.read_sql(query, engine)

print("Data from MySQL:")
print(df.head())

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df = df.dropna(subset=['order_date'])
df = df[df['order_amount'] > 0]

reference_date = df['order_date'].max() + pd.Timedelta(days=1)

rfm = df.groupby('customer_id').agg({
    'order_date': lambda x: (reference_date - x.max()).days,
    'customer_id': 'count',
    'order_amount': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']
rfm.reset_index(inplace=True)

rfm['CLV'] = rfm['Monetary']

print("\nRFM Table:")
print(rfm)

X = rfm[['Recency', 'Frequency', 'Monetary']]
y = rfm['CLV']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("RMSE:", rmse)
print("R² Score:", r2)
