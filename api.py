# APIs (application program interface)
# To work on APIs we need to use "requests" package.To install type(pip install requests)

# Let's work on itnues API
# for API visit (https://itunes.apple.com/search?entity=song&limit=1&term=weezer)
# Here limit=no.of songs,term = artist or singer name

# After visit above url a file is downloaded in .json(java script object notation) format

# ex:
"""
  "resultCount": 1,
  "results": [
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 5181689,
      "collectionId": 1526670332,
      "trackId": 1526670549,
      "artistName": "Manish Vyas",
      "collectionName": "Prasad",
      "trackName": "Prasad",
      "collectionCensoredName": "Prasad",
      "trackCensoredName": "Prasad",
      "artistViewUrl": "https://music.apple.com/us/artist/manish-vyas/5181689?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/prasad/1526670332?i=1526670549&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/prasad/1526670332?i=1526670549&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/72/c8/92/72c892d2-fc8b-4b8e-276e-709c0cbeea71/mzaf_2055100727158536783.plus.aac.p.m4a",
      "artworkUrl30": "https://is2-ssl.mzstatic.com/image/thumb/Music124/v4/16/db/fe/16dbfeed-7504-e430-f3e9-0cb3c981b545/191061822417_cover.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is2-ssl.mzstatic.com/image/thumb/Music124/v4/16/db/fe/16dbfeed-7504-e430-f3e9-0cb3c981b545/191061822417_cover.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is2-ssl.mzstatic.com/image/thumb/Music124/v4/16/db/fe/16dbfeed-7504-e430-f3e9-0cb3c981b545/191061822417_cover.jpg/100x100bb.jpg",
      "collectionPrice": 9.99,
      "trackPrice": 0.99,
      "releaseDate": "2005-09-01T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 6,
      "trackNumber": 1,
      "trackTimeMillis": 532040,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Worldwide",
      "isStreamable": true
    }
  ]
} """


# PRINT THAT JSON FILE BY USING requests library.

import requests
import sys
import json
if len(sys.argv) !=2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(json.dumps(response.json(),indent = 2))


# printing all songs of that singer or artist

import requests
import sys
import json
if len(sys.argv) !=2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
o = response.json()
for result in o["results"]:
    print(result["trackName"])
