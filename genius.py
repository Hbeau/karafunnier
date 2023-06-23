import requests
from bs4 import BeautifulSoup
from config import credentials
bearer_token = f"bearer {credentials['genius']['access-token']}"
def getGeniusLyrics(title,artist):
    searchResult = requests.get('https://api.genius.com/search',params={'q' : f"{title}"},headers={'authorization' : bearer_token})
    link = searchResult.json()['response']['hits'][0]['result']["path"]
    htmlResult = requests.get(f"https://genius.com{link}");
    soup = BeautifulSoup(htmlResult.text,features="html.parser");

    soup.select("[class*=LyricsHeader__Container]")[0].decompose();
    soup.select("[class*=Lyrics__Footer]")[0].decompose();
    for sideBar in soup.select("[class*=RightSidebar__Container]"):
            sideBar.decompose()
    for br in soup.find_all("br"):
        br.replace_with("\n")
    return soup.select("#lyrics-root")[0].text

