import requests
from bs4 import BeautifulSoup
from config import credentials
bearer_token = f"bearer {credentials['genius']['access-token']}"

def getGeniusLyrics(path):
    htmlResult = requests.get(f"https://genius.com{path}");
    soup = BeautifulSoup(htmlResult.text,features="html.parser");

    soup.select("[class*=LyricsHeader__Container]")[0].decompose();
    soup.select("[class*=Lyrics__Footer]")[0].decompose();
    for sideBar in soup.select("[class*=RightSidebar__Container]"):
            sideBar.decompose()
    for br in soup.find_all("br"):
        br.replace_with("\n")
    return soup.select("#lyrics-root")[0].text

def getGeniusSong(title):
    searchResult = requests.get('https://api.genius.com/search',params={'q' : f"{title}"},headers={'authorization' : bearer_token})
    if searchResult.status_code != 200:
         raise Exception("Unable to get Genius response")
    hits = searchResult.json()['response']['hits']
    songHit = list(filter(lambda hit : hit["type"] == "song",hits))
    if (len(songHit)>0) :
        return songHit[0]['result']
    raise Exception("Song not found on Genius")
