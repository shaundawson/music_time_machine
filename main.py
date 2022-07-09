import requests
import pprint
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

# playlist_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD:")

playlist_date = "2018-01-27"

billboard_url = f"https://www.billboard.com/charts/hot-100/{playlist_date}/"

response = requests.get(billboard_url)
content = response.text
soup = BeautifulSoup(content,"html.parser")

song_names = []

chart_results = soup.find_all(name="h3", class_="a-truncate-ellipsis")

for c in chart_results:
    song_title = c.getText().strip()
    song_names.append(song_title)

song_uris = []
year= playlist_date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pprint(f"{song} doesn't exist in Spotify. Skipped.")

    
