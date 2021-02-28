import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, 2:4]
kmeans = KMeans(n_clusters=3, random_state=0).fit_predict(X)
print(kmeans)
color = ("red", "blue", "green")
colors = np.array(color)[kmeans]
print(colors)
plt.scatter(X[:, 0], X[:, 1], c=colors)
plt.show()


cluster1 = np.random.uniform(0.5, 1.5, (2, 5))  # 生成（0.5,1.5）之间的随机数（2行5列）
cluster2 = np.random.uniform(3.5, 4.5, (2, 5))
X = np.hstack((cluster1, cluster2)).T  # 列拼接 并转置（10行2列）
print(X)
K = range(1, 6)
meandistortions = []  # 存放聚类中心列表
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)  # 拟合训练
    print(kmeans.cluster_centers_)
    # 任一点到 簇中心点（1,2,3,4,5）的最小距离（计算过程：求和再求平均值）
    meandistortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    print("第 {} 次-聚类中心".format(k))
    print(cdist(X, kmeans.cluster_centers_, 'euclidean'))

    print("第 {} 次聚类时----任一点到这{}个聚类中心其中一个的最小值".format(k, k))
    print(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1))

print(meandistortions)
plt.plot(K, meandistortions, 'bx-')  # 颜色blue，线条为-
plt.xlabel('k')

plt.ylabel('Ave Distor')  # plt.ylabel('平均畸变程度',fontproperties=font)
plt.title('Elbow method value K')  # plt.title('用肘部法则来确定最佳的K值',fontproperties=font);
plt.scatter(K, meandistortions)
plt.show()