import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn.cluster import KMeans
age = [2, 5, 4, 6, 3, 87, 134 , 146, 120, 112,15,13,16,11]
income = [521, 519, 524, 517, 16, 325, 315, 322, 321, 10,10,20,10,30]
data=list(zip(age,income))
inertias=[]
for i in range(1,11):
    Kmeans=KMeans(n_clusters=i)
    Kmeans.fit(data)
    inertias.append(Kmeans.inertia_)
# plt.plot(range(1,11),inertias,marker="o")
# plt.title("Inertia")
# plt.show()
Kmeans=KMeans(n_clusters=4)
Kmeans.fit(data)
centroids=Kmeans.cluster_centers_
plt.scatter(age,income,c=Kmeans.labels_)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X')
plt.show()
