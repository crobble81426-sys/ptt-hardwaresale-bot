import requests
from bs4 import BeautifulSoup
import os

PTT_URL = "https://www.ptt.cc/bbs/HardwareSale/index.html"
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
RECORD_FILE = "notified.txt"

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(PTT_URL, headers=headers, cookies={"over18":"1"})
soup = BeautifulSoup(res.text, "html.parser")

articles = soup.select(".r-ent .title a")

# 讀取已通知紀錄
if os.path.exists(RECORD_FILE):
    with open(RECORD_FILE, "r") as f:
        notified_links = set(f.read().splitlines())
else:
    notified_links = set()

for a in articles:
    title = a.text
    link = "https://www.ptt.cc" + a["href"]

    if "賣" in title and link not in notified_links:
        payload = {"content": f"硬體版新文章：{title}\n{link}"}
        requests.post(DISCORD_WEBHOOK, json=payload)

        # 更新紀錄檔
        with open(RECORD_FILE, "a") as f:
            f.write(link + "\n")

        break  # 只通知最新一篇
