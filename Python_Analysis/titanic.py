# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Data
df = pd.read_csv("train.csv")
print(f"Dataset shape: {df.shape}")

# Data Cleaning
# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)
# Fill missing Embarked with the mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
# Drop Cabin due to many missing values
df.drop(['Cabin'], axis=1, inplace=True)

# Feature Engineering
# Encode categorical variables
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
# Drop unneeded columns
df.drop(['Name', 'Ticket'], axis=1, inplace=True)

# Splitting Dataset
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[['Age', 'Fare']])
X_test_scaled = scaler.transform(X_test[['Age', 'Fare']])
X_train[['Age', 'Fare']] = X_train_scaled
X_test[['Age', 'Fare']] = X_test_scaled

# Logistic Regression Model
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)
print("Logistic Regression Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_lr):.2f}")
print(classification_report(y_test, y_pred_lr))

# Random Forest Model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.2f}")
print(classification_report(y_test, y_pred_rf))

# Hyperparameter Tuning for Random Forest
param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [5, 10, None]}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)
best_rf = grid.best_estimator_
y_pred_tuned = best_rf.predict(X_test)
print("Tuned Random Forest Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_tuned):.2f}")
print(classification_report(y_test, y_pred_tuned))

# Feature Importance (Random Forest)
importances = best_rf.feature_importances_
feature_names = X.columns
feature_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)
sns.barplot(x='Importance', y='Feature', data=feature_importances)
plt.title("Feature Importance (Random Forest)")
plt.show()
