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

        cover = soup.find("img", attrs={"class": "SizedImage__NoScript-sc-39a204ed-2 ZRulI"}).get("src")
        title = soup.find("span", attrs={"class": "SongHeader-desktop__HiddenMask-sc-9b4225cf-13 kHUuuE"}).get_text()

        info["cover"] = cover
        info["title"] = title


        

        return info
    except Exception as e:
        print(f"Error, song probably isn't part of an album on genius, workaround in the making\nError Code:\n {e}")

print("\n\nhttps://genius.com/ \n\n")
url = input("Please enter a URL from Genius: ")



giveInfo = getInfo(url)

strCover = str(giveInfo["cover"])

coverAscii = AsciiArt.from_url(strCover)


try:

    coverAscii.image = ImageEnhance.Contrast(coverAscii.image).enhance(2)
    coverAscii.image = ImageEnhance.Brightness(coverAscii.image).enhance(1.5)
    coverAscii.to_terminal(columns=225)

except Exception as e:
    print(f"Couldn't enhance image, defaulting to original \n Real Error Message: {e}")
    coverAscii.to_terminal(columns=225)



print("\n\n")

tprint(giveInfo["title"], font="rnd-xlarge")