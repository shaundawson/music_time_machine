import requests
from bs4 import BeautifulSoup

# playlist_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD:")

playlist_date = "2020-08-24"

spotify_url = f"https://www.billboard.com/charts/hot-100/{playlist_date}/"

response = requests.get(spotify_url)
content = response.text

soup = BeautifulSoup(content,"html.parser")

chart_results = soup.find_all(name="h3", class_="a-truncate-ellipsis")
for c in chart_results:
    song_title = c.getText().strip()
    print(song_title)







