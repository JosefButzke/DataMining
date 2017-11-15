from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1,2,3],[2,3,2],[4,5,2],[6,7,3]])

cores = ["g.","b.","b."]
clf = KMeans(n_clusters=2)

clf.fit(x)

centroids = clf.cluster_centers_
labels = clf.labels_
for i in range(len(x)):
    plt.plot(x[i][0],x[i][1],cores[labels[i]],markersize = 10)
plt.scatter(centroids[:,0], centroids[:,1],marker = 'x')

plt.show()
