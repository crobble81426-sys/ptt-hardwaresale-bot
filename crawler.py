import requests
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc/bbs/HardwareSale/index.html"

response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    cookies={
        "over18": "1"
    }
)

print("HTTP Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".title a")

print(f"找到 {len(titles)} 篇文章\n")

for article in titles:
    print(article.text)
