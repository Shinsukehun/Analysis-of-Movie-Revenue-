# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[2,4,6,8]
# plt.plot(x,y,label="y=2x",color="red",marker="o")
# plt.title("Line y=2x")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.grid(True)
# plt.show()
# import matplotlib.pyplot as plt
# category=["desktop","keyboard","mouse"]
# value=[3000,2000,1000]
# plt.bar(category,value, color="green")
# plt.title("Computer sale record")
# plt.xlabel("category")
# plt.ylabel("sales count")
# plt.show()
import matplotlib.pyplot as plt
import seaborn as sn
tips=sn.load_dataset("tips")
plt.figure(figsize=(8,5))
sn.scatterplot(data=tips,x="total_bill",y="tip", hue="sex",style="sex",s=100)
plt.title("Realtionship between Total Bill and Tip, Ground by sex", fontsize=14)
plt.xlabel("Total_Bill($)",fontsize=12)
plt.ylabel("Tip($)",fontsize=12)
plt.legend(title="sex",fontsize=10)
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()