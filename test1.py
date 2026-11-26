import requests
from bs4 import BeautifulSoup
import time

# 1. 要追蹤的股票代號（想改股票就在這裡增減）
stock = ["1101", "2330"]

# 2. 填入你第 1 步和第 2 步拿到的資料（記得保留雙引號 ""）
token = "9193820846:AAExyQiwrnctDacrv3KkPUvgExBNyIHnoWs"
chat_id = "9178728689"

for i in range(len(stock)):
    stockid = stock[i]
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 定位即時股價
    price = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ]).getText()
    
    # 發送 Telegram 訊息
    message = "股票 " + stockid + " 即時股價為 " + price
    send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(send_url)
    
    # 每次暫停 3 秒避免被網站阻擋
    time.sleep(3)
