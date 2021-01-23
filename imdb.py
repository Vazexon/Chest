import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import json
from rrr import key

with open('imdb_most_popular_movies_dump.json') as file:
    data = file.read()[3: ]
    js = json.loads(data)
    serviceurl = 'http://www.omdbapi.com/?plot=full&' + key
    print(key)
    with open('imdb_most_popular_movies.json', 'w+') as f:
        rank = 1
        for item in js:
            title = item['Rank & Title'].split('\n')[0]
            url = serviceurl + urllib.parse.urlencode(
                {"t": title})
            data = urlopen(url).read().decode()
            info = json.loads(data)
            info["Rank"] = rank
            print(type(item))
            json.dump(info, f, indent=4)
            print("_____________")
            rank += 1
