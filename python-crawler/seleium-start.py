from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#設定chrome driver 的執行檔路徑
options = Options()
options.chrome_executable_path="/Users/wuanjie/Desktop/python/chromedriver"
#建立driver 物件實體，用程式操作瀏覽器操作
driver=webdriver.Chrome(options=options)


#連線到ptt股票版
#取得股票版中的文章標題
driver.get("https://www.ptt.cc/bbs/Stock/index.html")

#print(driver.page_source)# 取得網頁原始碼
tags=driver.find_elements(By.CLASS_NAME,"title") # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)
    
#取得上一頁的文章標題
link= driver.find_element(By.LINK_TEXT,"‹ 上頁")
link.click() # 模擬使用者點擊標籤
tags=driver.find_elements(By.CLASS_NAME,"title") # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)
driver.close()

