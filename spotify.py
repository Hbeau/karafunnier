import spotipy
from config import credentials
from spotipy.oauth2 import SpotifyClientCredentials

SCOPE = "user-library-read"

auth_manager = SpotifyClientCredentials(client_id=credentials['spotify']["client-id"],client_secret=credentials['spotify']["client-secret"])
sp = spotipy.Spotify(auth_manager=auth_manager)
def music_statistics(title,artist):
    search_result = sp.search(f"{title} artist:{artist}")["tracks"]["items"]
    if len(search_result)>0 :
        track = search_result[0]
        track_id = track["id"]
        audio_feature = sp.audio_features(tracks=track_id)[0]
        return {
            'duration' : audio_feature['duration_ms'],
            'dancability' : audio_feature['danceability'],
            'energy' : audio_feature['energy'],
            'speechiness' : audio_feature['speechiness']
        }
    raise Exception("Song not found on Spotify")
