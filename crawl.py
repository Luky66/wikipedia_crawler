import requests
from bs4 import BeautifulSoup

# https://www.instagram.com/luky_66/

def insta_friend_spider(max_photos):
    url = "https://pixabay.com/en/users/melancholiaphotography-2312503/"
    html = requests.get(url)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, "lxml")

    for item in soup.find_all("div", {"class": "item"}):
        src = item.a.img.get("src")
        print(src)


print("Hello World")
insta_friend_spider(5)