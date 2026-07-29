import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Data
data = {
    "hours": [1, 2, 3, 4, 5],
    "score": [50, 55, 65, 70, 80]
}
df = pd.DataFrame(data)

# Step 2: Input (X) and output (y)
X = df[["hours"]]   # double brackets = keeps it as a table
y = df["score"]

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict
prediction = model.predict([[3.5]])
print(prediction)