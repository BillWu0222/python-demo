import matplotlib.pyplot as plt
import pandas as pd
#from sklearn import datasets
import numpy as np

# 先做出 X 軸跟 Y 軸的資料
x = [1, 2, 3]
y = [-4, 0, 8]
x2 = [1, 3, 3.5]
y2 = [-2, 3, -1]

# plt.plot 把 X 軸跟 Y 軸的資料給函數，就能畫折線圖
# plt.plot(x, y, label='Line 1')
plt.plot(x, y, 'ro-', label='line 1') # 要給他名字 這條線的名稱 'ro-' r代表顏色 o-代表線跟線之間給他一槓
#plt.plot(y=y,x=x, label='Line 1') #不能這樣


plt.plot(x2, y2, label='Line 2')

# plt.title 能改 figure 的標題
plt.title("Plotting two simple lines")

# plt.grid 能設定要不要網格
plt.grid(True)

# plt.xlabel 跟 plt.ylabel 能設定 X 軸和 Y 軸的名稱
plt.xlabel("X-label")
plt.ylabel("Y-label")

# plt.xlim 跟 plt.ylim 能設定 X 軸和 Y 軸的數值範圍
# 不會一開始就設定 會等畫完圖再來調整它
plt.xlim([0, 4])
plt.ylim([-5, 10])

# plt.legend 能設定要不要顯示圖例
plt.legend()

# 最後用 plt.show 就能把圖畫出來 
plt.show()
