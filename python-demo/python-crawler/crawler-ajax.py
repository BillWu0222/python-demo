#抓取medium.com的文章資料
import urllib.request as req
import ssl

# 禁用 SSL 驗證
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

url="https://medium.com/_/api/home-feed"

#建立一個request物件，附加headers的資訊
request=req.Request(url, headers={ #模擬網頁使用者的瀏覽行為，很多網頁都會擋爬蟲
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}) 

with req.urlopen(request,context=ssl_context) as response:
    data = response.read().decode("utf-8")  #根據觀察，取得的資料是json格式
 
#解析json格式的資料，取得每篇文章的標題
import json
data=json.load(data) #把原始json資料 解析成字典/列表的表現形式
posts= data["payload"]["references"]["Post"] 
for key in posts:
    post=posts[key]
    print(post["title"])
