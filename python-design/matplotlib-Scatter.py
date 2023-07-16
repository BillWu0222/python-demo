import gdown
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets 
url = 'https://drive.google.com/uc?id=17dfYDn1FD7y0Tbhkk8IymASemy6BuRNv'
output = 'Salary_data.csv'
gdown.download(url, output, quiet=False)

# 讀取薪水資料集
data = pd.read_csv("Salary_data.csv")
data.head()

# 先準備 X 軸跟 Y 軸的資料
X = data["YearsExperience"]
Y = data["Salary"]

# plt.scatter 把 X 軸跟 Y 軸的資料給他，就能畫散佈圖
plt.scatter(X, Y)

plt.title("Scatter Plot")
plt.xlabel("Working Experience (years)")
plt.ylabel("Annual Wage (dollars)")
plt.show()
