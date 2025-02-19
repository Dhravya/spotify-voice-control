from spotipy import Spotify

# catching errors
class InvalidSearchError(Exception):
    pass

def get_album_uri(spotify: Spotify, name: str):
    '''
    returns the uri of the album with the given name
    '''
    results = spotify.search(q=name, type="album")
    if len(results["albums"]["items"]) == 0:
        raise InvalidSearchError(f"No albums found with name: {name}")
    return results["albums"]["items"][0]["uri"]
    
def get_track_uri(spotify: Spotify, name: str):
    '''
    returns the uri of the track with the given name
    '''
    results = spotify.search(q=name, type="track")
    if len(results["tracks"]["items"]) == 0:
        raise InvalidSearchError(f"No tracks found with name: {name}")
    return results["tracks"]["items"][0]["uri"]

def get_artist_uri(spotify: Spotify, name: str):
    '''
    returns the uri of the artist with the given name
    '''
    results = spotify.search(q=name, type="artist")
    if len(results["artists"]["items"]) == 0:
        raise InvalidSearchError(f"No artists found with name: {name}")
    return results["artists"]["items"][0]["uri"]

def play_album(spotify: Spotify, uri: str):
    '''
    plays the album with the given uri
    '''
    spotify.start_playback(context_uri=uri)
    print("Playing on Spotify...")

def play_track(spotify: Spotify, uri: str):
    '''
    plays the track with the given uri
    '''
    spotify.start_playback(uris=[uri])
    print("Playing on Spotify...")

def play_artist(spotify: Spotify, uri: str):
    '''
    plays the artist with the given uri
    '''
    spotify.start_playback(context_uri=uri)
    print("Playing on Spotify...")
