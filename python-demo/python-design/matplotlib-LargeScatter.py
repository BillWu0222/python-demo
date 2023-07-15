import gdown
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets 

# 分類問題的資料集也很適合用這種方式來觀察分佈狀況
iris = datasets.load_iris() #現有的資料來分析
X_iris = iris.data
Y_iris = iris.target
n_classes = 3
for i in range(n_classes):
    plt.scatter(X_iris[Y_iris == i, 0], X_iris[Y_iris == i, 1],  
    label=iris.target_names[i])
plt.legend()
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
print(iris)