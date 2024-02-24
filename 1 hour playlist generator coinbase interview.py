# DJ a livestream for tim cook
# must use apple products to build tracklist

# Use artists
#   beatles 
#   journey
#   elvis

# return 10 songs for each artist
# Remove songs that contain explicit content
# build a shuffle function for each artist
# make a songlist that fits into a 1 hour time window

import json
import random
import requests


def getSongs (artist):
    # Get param includes no explcit content, only 10 items, and only songs: 
    requestURL = "https://itunes.apple.com/search?&media=music&entity=song&explicit=N&limit=10&term=" + artist
    HTTPresponse = requests.get(requestURL)
    return json.loads(HTTPresponse.content)

def shuffleSongs(songList):
    return random.shuffle(songList)


beatlesSongs = getSongs("beatles")
journeySongs = getSongs("journey")
elvisSongs   = getSongs("elvis")
allSongs     = beatlesSongs + journeySongs + elvisSongs # Make a big list of all playlist candidates
allSongs     = shuffleSongs(allSongs)                   # Shuffle the list so each artist has a fair chance of appearing in the playlist


playlistDuration = 0                                # How long the playlist is if you add all the songs up.
finalPlaylist    = []                               # Final playlist array for Tim Cook.
for i in allSongs:                                # Iterate through each song...
    trackTime = allSongs[i].trackTimeMillis / 1000  # Convert this song's duration from milliseconds to seconds
    if (playlistDuration + trackTime) <= 3600:      # If the song fits into the playlist...
        finalPlaylist += allSongs[i]                # Then add the song to playlist
        playlistDuration += trackTime               # And keep track of the current playlist duration
    else:
        # Do nothing, allows us to loop through. Maybe there is a smaller song that will fit.

print("Random playlist: ")
for i in finalPlaylist:
    print(finalPlaylist[i].trackName + " " + finalPlaylist[i].artistName) # Print each track and artist name
