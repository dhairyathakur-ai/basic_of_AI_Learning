from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

digits = load_digits()
print(digits.data.shape)   # (1797, 64) -> 1797 photos, 64 numbers each

# Step 2: Look at one photo
plt.imshow(digits.images[0], cmap="gray")
plt.title("Label: " + str(digits.target[0]))
plt.show()

# Step 3: Set up input (X) and output (y)
X = digits.data      # the photos (as numbers)
y = digits.target     # the correct digit for each photo

# Step 4: Split into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train the model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Step 6: Test how accurate it is
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Step 7: Try it on one specific photo
sample = X_test[0]
plt.imshow(sample.reshape(8, 8), cmap="gray")
plt.title("Model predicted: " + str(model.predict([sample])[0]))
plt.show()