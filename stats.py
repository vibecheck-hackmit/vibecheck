import numpy as np
#using: array

import spotify as sp
#using: 

def get_avg_mood_vec() -> np.array:
    tracks = np.array([ [ x.danceability, x.energy ,x.valence ] for x in sp.get_top_tracks_features() ])
    bulk_sum = tracks.sum(axis=0)
    return np.array([ x/tracks.shape[0] for x in bulk_sum])

if __name__ == '__main__':
    print(get_avg_mood_vec())

