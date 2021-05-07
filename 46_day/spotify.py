from API_KEY import SPOTIFY_CLIET_ID, SPOTIFY_CLIENT_SECRET
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from pprint import pprint
SPOTIPY_CLIENT_ID = SPOTIFY_CLIET_ID
SPOTIPY_CLIENT_SECRET = SPOTIFY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = 'http://example.com'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-private',
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               show_dialog=True,
                                               cache_path='token.txt'))

# user_id = sp.current_user()["id"]
# name = sp.current_user()['display_name']
# print(name)
a = sp.search(q='song:Miss You Much', type = 'track')
pprint(a)