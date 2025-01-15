import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df["Profit Revenue"]=(df['Revenue']-df['Budget'])/df['Budget']*100
print(df)
correlation=df["Rating"].corr(df["Revenue"])
print(f"{correlation:.2f}")
plt.scatter(df['Rating'],df['Revenue'])
plt.title("Rating vs Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue")
plt.show()