import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


file = pd.read_csv("iris2D.csv");
iris = file.iloc[:,[1,2]].values


clusters = 3;
iris_size = len(iris);

kmeans = KMeans(n_clusters=clusters);
kmeans.fit(iris)
y_kmeans = kmeans.predict(iris)


plt.scatter(iris[:,0],iris[:,1], c=y_kmeans,s=50,cmap="viridis")
centers = kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='black',s=200,alpha=0.4)
plt.xlabel("PC1");
plt.ylabel("PC2");
plt.title("Wynik grupowania kmeans=3")
plt.show()




scaler = StandardScaler()
x_scale = scaler.fit_transform(iris)

dbs = DBSCAN(eps=0.40,min_samples=10,metric="euclidean");
clusters = dbs.fit_predict(x_scale)


plt.scatter(iris[:,0],iris[:,1],c=clusters,cmap='viridis')
plt.xlabel("Bottom")
plt.ylabel("Left")
plt.title("Title")
plt.show()





