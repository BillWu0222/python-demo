import gdown
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets 
import numpy as np
iris = datasets.load_iris()
X_iris = iris.data
Y_iris = iris.target
average = X_iris[Y_iris == 0].mean(axis=0)

# 我們也可以一次看三種花的各個特徵的平均值，比較一下每種花是不是有某種傾向，不過這樣做圖會需要比較複雜一點的程式碼
n_classes = 3
averages = []
for i in range(n_classes):
    averages.append(X_iris[Y_iris == i].mean(axis=0))
print(averages)

fig = plt.figure(figsize=(10,10)) #建立畫布
ax = fig.add_subplot() #畫布上增加多張小圖 ，然後可以把小圖的位置資訊存到ax中

x = np.arange(len(iris.feature_names))
print(x)

bar1 = ax.bar(x - 0.25, averages[0], 0.25, label=iris.target_names[0])
bar2 = ax.bar(x    , averages[1], 0.25, label=iris.target_names[1])
bar3 = ax.bar(x + 0.25, averages[2], 0.25, label=iris.target_names[2])
ax.set_xticks(x) #設立x間的間距 
ax.set_xticklabels(iris.feature_names)

plt.legend()
plt.title("Bar Chart Iris Averages")
plt.ylabel("Average")
plt.tight_layout()
plt.show()