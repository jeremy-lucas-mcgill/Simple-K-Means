import numpy as np
import matplotlib.pyplot as plt
from data import Data
from kmeans import KMeans

data = Data(x_min=-100,x_max=100,y_min=-1,y_max=1,clusters=5,points_per_cluster=[50,100],scale=1,offset=[0,0])
clf = KMeans(num_clusters=2)
clusters,cluster_list = clf.fit(data=data,iterations=100)
print("Fit: ", clusters)
colors = ['blue','red','green','yellow','cyan','magenta','black','white','orange','purple']
plt.figure(figsize=(16,8))
for index in range(len(clusters)):
    if len(cluster_list[index]) > 0:
        x,y = zip(*cluster_list[index])
        plt.scatter(x,y,color = colors[index])
plt.show()

