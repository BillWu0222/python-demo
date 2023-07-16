# command + / 一次選取多行註解
# #定義裝飾器
# def myDeco(callback):
#     def run():
#         print("裝飾器中的程式碼")
#         callback(5) #這個回呼函示，其實就是被裝飾的普通函式
#     return run
# #使用裝飾器
# @myDeco
# def test(n):
#     print("普通函式的程式碼",n)
    
# test()

# 定義一個裝飾器，計算1+2+...+50 的總和
def cal(callback):
    def run():
        # 定義裝飾器想要執行的程式碼  裝飾器只負責做運算 不負責顯示
        result=0 
        for n in range(51):
            result+=n
        # （print(result) #印出1+2+...+50的總和）
        # 把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run
# 使用裝飾器
@cal
def show(n):
    print("計算結果是:",ｎ)

show()
        