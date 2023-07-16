import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gdown 
url = 'https://drive.google.com/uc?id=1LALbA30NdFeOZxe06iYSUlQEDCPyDDpY'
output = 'recent-grads.csv'
gdown.download(url, output, quiet=False)
df = pd.read_csv("recent-grads.csv")
#df.info()
#print(df)

# 檢視[排名1至173的科系]的[收入]變化
# plot預設是畫折線圖
#df.plot(x="Rank", y=["P25th", "Median", "P75th"])
#plt.show()

# 檢視[系所收入中位數]與[失業人數比例]的關係
# 將 plot 裡的 kind 參數設為 scatter 就能畫出散佈圖
df.plot(x="Median", y="Unemployment_rate", kind="scatter")
#df.plot(x="Median", y="Unemployment_rate")
plt.show()

rank=df.sort_values(by="Median", ascending=False).head()
print(rank)