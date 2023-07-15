#抓取ptt八卦版的網頁原始碼（html) 
import urllib.request as req
import ssl

# 禁用 SSL 驗證
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
def getData(url):
    #建立一個request物件，附加headers的資訊
    request=req.Request(url, headers={ #模擬網頁使用者的瀏覽行為，很多網頁都會擋爬蟲
        "cookie":"over18=1",  #網頁瀏覽器會存cookie～
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }) 

    with req.urlopen(request,context=ssl_context) as response:
        data = response.read().decode("utf-8")   
    
    #解析原始碼，取得每篇文章的標題

    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles= root.find_all("div",class_="title") #尋找class="title"的div標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)
    #抓取上一頁連結     
    nextLink= root.find("a",string="‹ 上頁") #找到內文是‹ 上頁 的 a 標籤
    return nextLink["href"]
PageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    PageUrl="https://www.ptt.cc/"+ getData(PageUrl)
    count+=1

