# Calculate the mean, median, and mode of the list [4, 7, 2, 7, 8, 10, 7].
# import numpy as np
# from scipy.stats import mode
# data=[4, 7, 2, 7, 8, 10, 7]
# datamean=np.mean(data)
# datamedian=np.median(data)
# mode_result=mode(data)
# print(f"{datamean}, {datamedian}, {mode_result[0]}")

# Generate 1,000 random values from a normal distribution and plot its histogram.
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.randn(1000)
# plt.figure(figsize=(8,5))
# plt.hist(x,bins=100,density=True,alpha=0.5,color="g")
# plt.title("Normal distribution")
# plt.show()

# Calculate the correlation coefficient and covariance for two lists: x = [1, 2, 3, 4, 5] and y = [5, 4, 3, 2, 1].
# import numpy as np
# x = [1, 2, 3, 4, 5]
# y = [5, 4, 3, 2, 1]
# corr=np.corrcoef(x,y)[0,1]
# print(corr)
import numpy as np
import matplotlib.pyplot as plt
rolls=np.random.randint(1,7,size=1000)
unique,count=np.unique(rolls, return_counts=True)
plt.bar(unique,count,align="center",alpha=0.5,color="g")
plt.title("Frequence of Each Die face in 1000 Rolls")
plt.xlabel("Die Face")
plt.ylabel("Frequence")
# plt.xticks(unique)
plt.show()