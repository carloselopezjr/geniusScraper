from ascii_magic import AsciiArt
from PIL import ImageEnhance
import requests
from bs4 import BeautifulSoup
from art import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Accept-Language": "en-US,en;q=0.5"
}

def getInfo(url: str) -> dict:

    info = {}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, features="html.parser")

    try:

        cover = soup.find("img", attrs={"class": "SizedImage__Image-sc-39a204ed-1 dycjBx SongHeader-desktop__SizedImage-sc-9b4225cf-15 dsPjCq"}).get("src")
        title = soup.find("span", attrs={"class": "SongHeader-desktop__HiddenMask-sc-9b4225cf-13 kHUuuE"}).get_text()
        lyrics = soup.find("div", attrs={"class": "Lyrics__Container-sc-3d1d18a3-1 bjajog"}).get_text()

        info["cover"] = cover
        info["title"] = title
        info["lyrics"] = lyrics

        

        return info
    except Exception as e:
        print(f"error:\n {e}")


url = input("Please enter a URL from Genius: ")

giveInfo = getInfo(url)

print(giveInfo)