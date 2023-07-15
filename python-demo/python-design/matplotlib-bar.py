import gdown
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets 
# 長條圖可以用來看多個類別的狀況，這邊來看一下 Setosa 這種花的各個 feature 的平均值
iris = datasets.load_iris()
X_iris = iris.data
Y_iris = iris.target
average = X_iris[Y_iris == 0].mean(axis=0)
print(average)

# plt.bar 把 X 軸跟 Y 軸的資料給他，就能畫長條圖，注意 X 軸會是多個不連續的數值或類別
plt.bar(iris.feature_names, average)
plt.title("Bar Chart Setosa Averages")
plt.ylabel("Average (in cm)")

# plt.tight_layout 防止圖裡的字疊在一起
plt.tight_layout()
plt.show()