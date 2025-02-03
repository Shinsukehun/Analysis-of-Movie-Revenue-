import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

df=pd.read_csv("train.csv")

df["Sex"]=df["Sex"].map({"male":0,"female":1})
df["Age"].fillna(df["Age"].median(),inplace=True)
features=["Pclass", "Sex", "Age", "Fare"]
x = df[features]
y=df["Survived"]

x_train,x_test, y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(x_train, y_train)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)

xgb_model=XGBClassifier(enable_categorical=True,eval_metric="logloss")
xgb_model.fit(x_train,y_train)

y_pred_rf = rf_model.predict(x_test)
y_pred_log = log_reg.predict(x_test)
y_pred_xgb = xgb_model.predict(x_test)

rf_acc = accuracy_score(y_test, y_pred_rf)
log_reg_acc = accuracy_score(y_test, y_pred_log)
xgb_acc = accuracy_score(y_test, y_pred_xgb)
print(f"XGBoost Accuracy: {xgb_acc:.4f}")
print(classification_report(y_test, y_pred_xgb))
print(f"Logistic Regression Accuracy: {log_reg_acc:.4f}")
print(classification_report(y_test, y_pred_log))
print(f"Random Forest Accuracy: {rf_acc:.4f}")
print(classification_report(y_test, y_pred_rf))
model_results = {
    "Logistic Regression": log_reg_acc,
    "Random Forest": rf_acc,
    "XGBoost": xgb_acc
}

# Print model accuracies
for model, acc in model_results.items():
    print(f"{model}: {acc:.4f}")
# log_reg=LogisticRegression(max_iter=1000)
# log_reg.fit(x_train,y_train)
# y_pred_log=log_reg.predict(x_test)
# log_reg_acc=accuracy_score(y_test,y_pred_log)
# print(f"Logistic Regression Accuracy:{log_reg_acc:.4f}")
# print(classification_report(y_test, y_pred_log))
# print(f"Training samples: {x_train.shape[0]}")
# print(f"Testing samples: {x_test.shape[0]}")
# df=pd.read_csv("train.csv")
# print(f"missing value\n{df.isnull().sum()}")
# df["Age"].fillna(df["Age"].median(),inplace=True)
# df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
# df.drop(columns=["Cabin"], inplace=True)
# print(f"missing value\n{df.isnull().sum()}")
# plt.figure(figsize=(10,6))

# sns.countplot(x="Sex",hue="Survived",data=df,palette="Set2")
# plt.title("Survival by Gender")
# plt.show()
# survival_rate=df["Survived"].mean()*100
# print(f"Survival Rate:{survival_rate:.2f}%")

# sns.histplot(df[df["Survived"]==1]["Age"],kde=True,color="green", label="Survived",bins=30)
# sns.histplot(df[df["Survived"]==0]["Age"],kde=True,color="red", label="Not Survived",bins=30)
# plt.legend()
# plt.title("Age Distribution by Survival Status")
# plt.xlabel("Age")
# plt.ylabel("Count")

# sns.countplot(x="Pclass",hue="Survived",data=df,palette="Set1")
# plt.show()

# df["FamilySize"]=df["SibSp"]+df["Parch"]+1
# sns.countplot(x="FamilySize", hue="Survived", data=df, palette="muted")
# plt.title("Survival Rate by Family Size")
# plt.show()

# Correlation heatmap
# corr = df.select_dtypes(include=['number']).corr()
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()
