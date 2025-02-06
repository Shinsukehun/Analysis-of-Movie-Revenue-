import pandas as pd
import numpy as np
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Recency': [10, 30, 100, 5, 20],
    'Frequency': [5, 3, 2, 7, 4],
    'Monetary': [200, 500, 50, 1000, 300],
    'Age': [25, 40, 30, 35, 50]
}
df=pd.DataFrame(data)
print(df)
import matplotlib.pyplot as plt
import seaborn as sns

print(df.isnull().sum())
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Pairplot will be displayed on the first axis
sns.pairplot(df)
plt.subplots_adjust(wspace=0.3)  # Adjust spacing between the plots

# Correlation matrix and heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=axes[1])


plt.show()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Assume Monetary is the target CLV
X = df[['Recency', 'Frequency', 'Age']]  # Features
y = df['Monetary']  # Target (CLV)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')
import joblib

# Save the trained model to a file
joblib.dump(model, 'clv_model.pkl')
