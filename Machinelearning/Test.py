# Implement Linear Regression on a dataset with one feature (e.g., predicting house prices based on square footage). Evaluate the model using MAE, MSE, and R².
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# data = {
#     'Square Footage': [1500, 1800, 2000, 2500, 3000],
#     'House Price': [350000, 400000, 450000, 500000, 600000]
# }
# df=pd.DataFrame(data)
# footage=df[['Square Footage']]
# price=df['House Price']
# footage_train, footage_test, price_train, price_test=train_test_split(footage, price,test_size=0.2,random_state=42)
# model=LinearRegression()
# model.fit(footage_train,price_train)
# price_pred=model.predict(footage_test)

# plt.scatter(footage,price, color="red")
# plt.plot(footage, model.predict(footage), color="blue")
# plt.title("Predicting house prices")
# plt.grid(True)
# plt.show()
# mae=mean_absolute_error(price_test,price_pred)
# mse=mean_squared_error(price_test,price_pred)
# r2=r2_score(price_test,price_pred)
# print(f"Model coefficient:{model.coef_}")
# print(f"Model intercept:{model.intercept_}")
# print(f"{mae}, {mse}, {r2}")

#Implement Logistic Regression to classify a binary dataset (e.g., predict whether a customer will buy a product based on age and income). Evaluate the model using accuracy and confusion matrix.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay

data={
     'Age': [22, 45, 34, 50, 23, 40, 36, 28, 30, 60],
    'Income': [20000, 50000, 35000, 60000, 25000, 45000, 40000, 29000, 32000, 70000],
    'BuyProduct': [0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
}
df=pd.DataFrame(data)
x=df[["Age","Income"]]
y=df["BuyProduct"]
x_train,x_test, y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"Accurcy:{accuracy*100:.2f}%")
cm=confusion_matrix(y_test,y_pred)
cm_display=ConfusionMatrixDisplay(confusion_matrix=cm)
cm_display.plot(cmap="Blues")
plt.show()

