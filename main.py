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
    soup = BeautifulSoup(page.content, features="lxml")

    try:

        #cover = soup.find_all("img")
        cover = soup.find("img", attrs={"class": "SizedImage__NoScript-sc-39a204ed-2 ZRulI"}).get("src")
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

coverArt = str(giveInfo["cover"])

coverAscii = AsciiArt.from_url(coverArt)

coverAscii.to_terminal()
tprint(giveInfo["title"])