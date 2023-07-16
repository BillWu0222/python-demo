import pandas as pd
# 讀取資料

data = pd.read_csv("googleplaystore.csv") # 把CSV 格式的檔案讀取成一個 DataFrame 

# 觀察資料
# print("資料數量", data.shape)
# print("資料欄位", data.columns) 
# print("=================================================")

# # 分析資料
# condition = data["Rating"]<= 5  # 對資料做篩選 ， 因為發現評分平均大於五 有點不尋常 所以開始做清理的動作
# data= data[condition]
# print(data)

# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
print("取得前一百個應用程式的平均", data["Rating"].nlargest(100).mean())

#分析資料：安裝數量的各種統計數據 
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "", regex=True).replace("Free", ""))
#print(data["Installs"])
print("平均數", data["Installs"].mean())
condition = data["Installs"]> 100000
print("安裝數量大於十萬的應用程式有幾個",data[condition].shape[0])
 
#基於資料的應用：關鍵字搜尋應用程式的名稱
keyword =input("請輸入關鍵字：")
condition = data["App"].str.contains(keyword)
print(data[condition]["App"])