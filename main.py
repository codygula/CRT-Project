# main part of project
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from spotipy.oauth2 import SpotifyOAuth

from pprint import pprint
from time import sleep

# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
    




# ### This works
# scope = 'playlist-read-private'
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_playlists(limit=50)
# for i, item in enumerate(results['items']):
#     print("%d %s" % (i, item['name']))



### This also works. It will return 'devices' JSON object with two options. It crashes after running "change track" part
### Device needs to be "active." Unsure if this is doable with API. It will work when I have Spotify open in a browser. It will crash with 404 error if not.

### In order for device to be active, spotify seems to need to be open and recently playing something. 
### Device ID is not necessary. The API will start playing whatever the active device is, if there is one.
### Need try/except loop to elegantly handle not having active device.

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

# Change volume
sp.volume(100)
sleep(2)
sp.volume(50)
sleep(2)
sp.volume(100)



### This also works
# scope = "user-library-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])