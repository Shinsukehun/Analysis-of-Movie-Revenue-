# Normal distribution
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.normal(loc=0,scale=1,size=1000)
# plt.hist(x,bins=30,density=True,alpha=0.6,color='g')
# plt.title("Normal Distribution")
# plt.show()

# Binomial distribution
# import matplotlib.pyplot as plt
# from scipy.stats import binom
# n,p=10,0.5
# data=binom.rvs(n=n,p=p,size=1000)
# plt.hist(data,bins=10,density=True,alpha=0.6,color='g')
# plt.title("Binomial Distribution")
# plt.show()

# Correlation and Covariance
import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[200, 400, 600, 800, 1000]    
# correlation=np.corrcoef(x,y)[0,1]
covariance = np.cov(x, y,ddof=0)[0, 1]
print(f"{covariance}")