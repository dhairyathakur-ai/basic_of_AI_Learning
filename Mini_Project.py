# Mini Project: Analyze a small sales dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [100, 150, 130, 200, 90, 175],
    "expenses": [80, 90, 85, 120, 70, 95]
}

df = pd.DataFrame(data)
df["profit"]=df["sales"]-df["expenses"]
print(df)

total_sales = df["sales"].sum()
print(total_sales)

average_profit= df["profit"].mean()
print(average_profit)

best_month_index=df["profit"].idxmax()
print(best_month_index)

plt.plot(df["month"], df["sales"], label="Sales")
plt.plot(df["month"], df["expenses"], label="Expenses")
plt.title("Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.show()

average_profit = df["profit"].mean()
result = df[df["profit"]> average_profit]
print(result)