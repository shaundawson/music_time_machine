import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from keys import APP_CLIENT_ID, APP_CLIENT_SECRET, APP_REDIRECT_URI

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=APP_REDIRECT_URI,
        client_id=APP_CLIENT_ID,
        client_secret=APP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])


# playlist_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD:")

playlist_date = "2018-01-27"

spotify_url = f"https://www.billboard.com/charts/hot-100/{playlist_date}/"

response = requests.get(spotify_url)
content = response.text

soup = BeautifulSoup(content,"html.parser")

chart_results = soup.find_all(name="h3", class_="a-truncate-ellipsis")
for c in chart_results:
    song_title = c.getText().strip()
    print(song_title)