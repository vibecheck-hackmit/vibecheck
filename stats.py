import numpy as np
#using: array

import spotify as sp
#using: 

import typing as ty

import math

def category_vecs() -> ty.Tuple[np.array]:
    """vectors that represent categories of moods."""
    return (np.array([1,1,1]) #exhilirated joy
           ,np.array([1,1,0]) #passionate drive
           ,np.array([0,0,0]) #pensive solitude
           ,np.array([0,1,0]) #focused determination
           ,np.array([1,0,1]) #gentle elation
           ,np.array([0,0,1]) #calm contentment
           ,np.array([0.5,0.5,0.5]) #grounded equilibrium
           ,np.array([1,0.5,0]) #whimsical melancholy
           ,np.array([0.5,1,0.5]) #vigorous ambivalence
           ,np.array([0,0.5,1]) #serene positivity
           )


def get_avg_mood_vec() -> np.array:
    """returns a vector of the average danceability, energy, valence of a user's recent top songs on spotify."""

    #get top tracks and make vectors that represent mood.
    tracks = np.array([ [ x.danceability, x.energy, x.valence ] for x in sp.get_top_tracks_features() ])

    #get the sum of all rows in the matrix
    bulk_sum = tracks.sum(axis=0)
    
    #avg mood vector
    return np.array([ x/tracks.shape[0] for x in bulk_sum])

def categorize() -> int:
    """returns an int that represents why "category" is closest to a user's average mood vector."""

    avg = get_avg_mood_vec()
    
    #store the current minimum distance and index of the match in the category vectors.
    cur_min_dist, closest_match = float('inf'), None

    for index, vec in enumerate(category_vecs()):

        #calculate euclidean distance between average vector and current base vector.
        dist = math.sqrt( (avg[0]-vec[0])**2 + (avg[1]-vec[1])**2 + (avg[2]-vec[2])**2)

        if dist <= cur_min_dist:
            cur_min_dist = dist
            closest_match = index

    return closest_match

if __name__ == '__main__':
    print(categorize()) 

