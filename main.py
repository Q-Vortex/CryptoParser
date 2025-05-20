from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import mj
import config
import json
import time;
import datetime
import os

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except Exception:
    config.load_config()

cookie_str = config["COOKIE"]

cookies = []
for part in cookie_str.split('; '):
    if '=' in part:
        name, value = part.split('=', 1)
        cookies.append({
            'name': name,
            'value': value,
            'path': '/',
            'domain': 'tradingview.com'
        })


options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

driver.get("https://www.tradingview.com")
time.sleep(3)

for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Ошибка добавления cookie {cookie['name']}: {e}")

driver.get(config["URL"])

def infomake(info):
    for i in range(len(info)):
        info[i] = info[i].replace('\u2212', '-').replace('\u202f', '')

    signal_words = {"buy", "sell"}
    i = 1

    while i < len(info):
        if info[i] in signal_words:
            info[i - 1] = f"{info[i - 1]} {info[i]}"
            del info[i]
        else:
            i += 1

    del info[1]

    return info
    # if config["VISUALIZE"] == "true":
    #     print(f"ADD: {tag} {item}\nTIME: {jdate} {jtime}")



try:
    while True:
        os.system('clear')
            
        

        jdate = datetime.datetime.now().strftime("%d.%m.%Y")
        jtime = datetime.datetime.now().strftime("%H:%M:%S")

        if not config["VISUALIZE"] == "true":
            print("Working [", jdate, jtime, "]")
    
        head = driver.find_elements(By.CSS_SELECTOR, "tr.row-RdUXZpkv > th.cell-UhKtUaZw.cell-UhKtUaZw.cell-hdxjpvoX:not(:nth-child(1))")
        info = driver.find_elements(By.CSS_SELECTOR, "tr.row-RdUXZpkv.listRow")

        heads = []
        for h in head:
            heads.append(h.text.replace("\n", " "))

        for inf in info:
            items = infomake(inf.text.replace("\n", " ").split(" "))

            mj.add_to_dict(jdate, jtime, items, heads)

        time.sleep(int(config["DELAY_MIN"]) * 60)
except Exception as e:
    print("Ошибка при поиске элементов:", e)

finally:
    driver.quit()
