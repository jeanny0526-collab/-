import requests
from bs4 import BeautifulSoup
import time

# 1. 要追蹤的股票代號
stock = ["1101", "2330"]

# 2. 填入你的 token 和 chat_id（保留雙引號）
token = "9193820846:AAExyQiwrnctDacrv3KkPUvgExBNyIHnoWs"
chat_id = "9178728689"

# 偽裝成一般 Chrome 瀏覽器，避免被 Yahoo 股市封鎖
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

for stockid in stock:
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 尋找股價標籤
    price_tag = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ])
    
    if price_tag:
        price = price_tag.getText()
        message = f"股票 {stockid} 即時股價為 {price}"
    else:
        message = f"股票 {stockid} 抓不到價格，可能 Yahoo 網頁結構有變動"
        
    send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(send_url)
    time.sleep(3)
