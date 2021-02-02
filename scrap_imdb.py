import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from rrr import key

with open('imdb_most_popular_movies_dump.html') as file:
    soup = BeautifulSoup(file, "html.parser")
    tags = soup('td', attrs={'class': 'titleColumn'})
    serviceurl = 'http://www.omdbapi.com/?plot=full&' + key
    with open('imdb_most_popular_movies.json', 'w+') as f:
        rank = 1
        for tag in tags:
            title = tag.text.strip().split('\n')[0]
            url = serviceurl + urllib.parse.urlencode(
                {"t": title})
            data = urlopen(url).read().decode()
            info = json.loads(data)
            info["Rank"] = rank
            json.dump(info, f, indent=4)
            rank += 1
