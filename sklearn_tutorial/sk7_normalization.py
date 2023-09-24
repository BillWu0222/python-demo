# 導入所需的庫
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# 創建一個 3x3 的 NumPy 數組，包含不同範圍的數值
a = np.array([[10, 2.7, 3.6],
             [-100, 5, -2],
             [120, 20, 40]], dtype=np.float64)

# 輸出原始數組 a
print("Original array:")
print(a)

# 使用 preprocessing.scale 函式對數組進行標準化處理
# 標準化將每個特徵的平均值調整為 0，標準差調整為 1
scaled_a = preprocessing.scale(a)

# 輸出標準化後的數組 scaled_a
print("Scaled array:")
print(scaled_a)

# 使用 make_classification 生成一個合成的分類數據集
X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)

# 將數據集 X 的特徵繪製在散點圖上，按照目標標籤 y 進行著色

# X 是一個包含特徵的數據集，每一列代表一個特徵
# X[:, 0] 表示取所有行（樣本），但只取第一列（第一個特徵）的數據
# X[:, 1] 表示取所有行，但只取第二列（第二個特徵）的數據

# 使用 plt.scatter 函式繪製散點圖
# 第一個參數是 x 軸的數據，這裡是第一個特徵 X[:, 0]
# 第二個參數是 y 軸的數據，這裡是第二個特徵 X[:, 1]
# c 參數表示顏色，這裡根據目標標籤 y 來決定散點的顏色
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

# 使用 preprocessing.scale 函式對數據集進行標準化處理（正規化）
X = preprocessing.scale(X)

# 將數據集分割為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

# 創建一個支持向量機（SVM）分類器
clf = SVC()

# 在訓練集上訓練 SVM 分類器
clf.fit(X_train, y_train)

# 計算並輸出 SVM 分類器在測試集上的分類準確度
accuracy = clf.score(X_test, y_test)
print("Classification accuracy:", accuracy)
