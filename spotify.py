import json
import spotipy
import numpy as np
from spotipy.oauth2 import SpotifyOAuth

def get_top_tracks_features():
    # Load client ID and secret from .creds/spotify.json file
    with open('.creds/spotify.json', 'r') as f:
        creds = json.load(f)
        CLIENT_ID = creds['CLIENT_ID']
        CLIENT_SECRET = creds['CLIENT_SECRET']

    # Set up authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8888/callback", 
        scope=["user-top-read"]
    ))

    # Fetching top 10 tracks from the last month
    time_range = 'short_term'  
    results = sp.current_user_top_tracks(limit=10, time_range=time_range)

    # Get track IDs
    track_ids = [track['id'] for track in results['items']] 

    # Fetch audio features for these tracks
    audio_features = sp.audio_features(track_ids)

    # Create a list of tuples with the results
    tracks_info = []
    for track, feature in zip(results['items'], audio_features):
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        danceability = feature['danceability']
        energy = feature['energy']
        valence = feature['valence']
        
        tracks_info.append([track_name, artist_name, danceability, energy, valence])

    # Close the Spotify session
    sp = None

    # Convert to numpy array and return
    return np.array(tracks_info, dtype=object)

tracks_data = get_top_tracks_features()
for idx, track in enumerate(tracks_data):
    track_name, artist_name, danceability, energy, valence = track
    print(f"{idx+1}. {track_name} by {artist_name}")
    print(f"Danceability: {danceability}, Energy: {energy}, Valence: {valence}\n")
