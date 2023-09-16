import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Track: 
    def __init__(self, track_name, artist_name, danceability, energy, valence, mode):
        self.track_name = track_name
        self.artist_name = artist_name
        self.danceability = danceability
        self.energy = energy
        self.valence = valence
        self.mode = mode

    def __repr__(self):
        return f"Track(name={self.track_name}, artist={self.artist_name}, danceability={self.danceability}, energy={self.energy}, valence={self.valence}, mode={self.mode})"

def get_top_tracks_features():
    with open('.creds/spotify.json', 'r') as f:
        creds = json.load(f)
        
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=creds['CLIENT_ID'],
        client_secret=creds['CLIENT_SECRET'],
        redirect_uri="http://localhost:8888/callback", 
        scope=["user-top-read"]
    ))

    results = sp.current_user_top_tracks(limit=10, time_range='short_term')
    audio_features = sp.audio_features([track['id'] for track in results['items']])

    # Create a list of objects
    tracks_info = []
    for track, feature in zip(results['items'], audio_features):
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        danceability = feature['danceability']
        energy = feature['energy']
        valence = feature['valence']
        mode = feature['mode']
        
        track_obj = Track(track_name, artist_name, danceability, energy, valence, mode)
        tracks_info.append(track_obj)

    return tracks_info

# Test
if __name__ == "__main__":
    tracks = get_top_tracks_features()
    for track in tracks:
        print(track)