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

#1
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction:", prediction[0])
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

#2
from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(20).reshape(10, 2)
y = np.arange(10)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

#3
from sklearn.tree import DecisionTreeClassifier

X = [
    [22, 1],
    [25, 0],
    [47, 1],
    [52, 0],
    [46, 1]
]

y = ["Yes", "No", "Yes", "No", "Yes"]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[30, 1]])

print("Prediction:", prediction[0])

#4
from sklearn.linear_model import LogisticRegression

X = [
    [2],
    [4],
    [6],
    [8],
    [10]
]

y = [0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[5]]))


#5
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "temp": [___],
    "sold": [___]
}
df = pd.DataFrame(data)

X = ___
y = ___

model = ___
model.___(X, y)

prediction = model.predict([[___]])
print(prediction)
