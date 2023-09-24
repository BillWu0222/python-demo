import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn import datasets
from sklearn.preprocessing import LabelEncoder

np.random.seed(7)
iris = datasets.load_iris()

# 將特徵數據轉換為Pandas的DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# 定義目標變量映射字典，將目標變量值與對應的類別標籤進行映射
target_mapping = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

# 將目標變量列設置為鳶尾花數據集的目標變量，並使用map()方法進行映射操作
df["Species"] = iris.target
df["Species"] = df["Species"].map(target_mapping)

# 創建LabelEncoder對象，並使用它將目標變量列中的類別標籤編碼為整數
encoder = LabelEncoder()
df["Species"] = encoder.fit_transform(df["Species"])

# 將DataFrame轉換為NumPy數組並隨機打亂數據
dataset = df.values
np.random.shuffle(dataset)

# 從打亂後的數據集中獲取特徵和目標變量
x = dataset[:, 0:4].astype(float)  #這行程式碼從數據集中選取所有行的前四列作為特徵數據。[:, 0:4] 表示選取所有行的第0至第3列（總共四列）。.astype(float) 則將選取的數據轉換為浮點數型態，這是因為在神經網絡中通常需要將數據以數值形式表示。
y = to_categorical(dataset[:, 4])  #這行程式碼從數據集中選取所有行的第四列作為目標變量。[:, 4] 表示選取所有行的第4列（從0開始計數）。to_categorical 函數將目標變量轉換為獨熱編碼的形式，這對於多類別分類問題是常見的處理方式。獨熱編碼會將目標變量的每個值轉換為一個二進制向量，其中只有目標類別對應的元素為1，其它元素為0。

# 特徵標準化，將特徵數據進行均值為0，標準差為1的標準化處理
x -= x.mean(axis=0)
x /= x.std(axis=0)

# 將數據集劃分為訓練集和測試集
x_train, y_train = x[:120], y[:120]
x_test, y_test = x[120:], y[120:]

model = Sequential()#創建一個Sequential模型物件。Sequential模型是Keras中的一種基本模型類型，它按照順序逐層添加網絡層。
# 添加Dense層，構建多層感知機模型
model.add(Dense(6, input_shape=(4,), activation="relu"))# 輸入層 添加一個Dense層作為輸入層。Dense層是神經網絡中最常見的一種層，每個神經元與上一層的所有神經元相連。在這裡，我們定義了6個神經元，並指定輸入的形狀為(4,)，表示有4個輸入特徵。激活函數選擇為ReLU
model.add(Dense(6, activation="relu"))# 隱藏層
model.add(Dense(3, activation="softmax")) # 輸出層 添加一個Dense層作為輸出層。輸出層的神經元數量根據問題的類別數量而定。在這裡，我們有3個類別，因此定義了3個神經元。激活函數選擇為Softmax，用於多分類問題，它將輸出轉換為每個類別的概率分佈
#通過添加這些Dense層，我們構建了一個具有輸入層、隱藏層和輸出層的多層感知機模型。每個Dense層都包含一組權重和偏差項，這些參數將在訓練過程中學習以適應給定的數據和目標。

# 編譯模型，設置損失函數、優化器和評估指標
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

print("Training....")
model.fit(x_train, y_train, epochs=100, batch_size=5)

print("Testing....")
loss,accuracy =model.evaluate(x_test,y_test)

print("準確度={:.2f}".format(accuracy))

print("Saving Model :iris.h5. . . ")
model.save("iris.h5")

from tensorflow import keras
model = Sequential()
model = keras.models.load_model("iris.h5")
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

loss, accuracy = model.evaluate(x_test, y_test)
print("測試資料集的準確度={:.2f}".format(accuracy))

y_pred_prob = model.predict(x_test)
y_pred = np.argmax(y_pred_prob, axis=1) # 根据最高概率选择類別

print(y_pred)

y_target = dataset[:, 4][120:].astype(int)

cm = pd.crosstab(y_target, y_pred, rownames=["Actual"], colnames=["Predict"])
print(cm)