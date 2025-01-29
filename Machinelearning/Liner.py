import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Example dataset
X = np.array([[1], [2], [3], [4], [5]])  # Features (independent variable)
y = np.array([1, 2, 3, 4, 5])  # Target (dependent variable)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
print(y_pred)
# Plot the results
plt.scatter(X, y, color="blue")  # Data points
plt.plot(X, model.predict(X), color="red")  # Model's prediction line
plt.title("Linear Regression Example")
plt.grid(True)
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# Model evaluation
print(f"Model coefficients: {model.coef_}")
print(f"Model intercept: {model.intercept_}")
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
