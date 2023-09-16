import numpy as np
#using: array

import spotify as sp
#using: 

import typing as ty

import enum

def basis_mood_vecs() -> ty.Tuple[np.array]:
    return (np.array([1,1,1])
           ,np.array([1,1,-1])
           ,np.array([-1,-1,1])
           ,np.array([-1,1,-1])
           ,np.array([1,-1,1])
           ,np.array([-1,-1,1])
           ,np.array([0,0,0])
           ,np.array([1,0,-1])
           ,np.array([0,1,0])
           ,np.array([-1,0,1])
           )


def get_avg_mood_vec() -> np.array:

    #get top tracks and make vectors that represent mood.
    tracks = np.array([ [ x.danceability, x.energy, x.valence ] for x in sp.get_top_tracks_features() ])

    #get the sum of all rows in the matrix
    bulk_sum = tracks.sum(axis=0)
    
    #return the avg mood vector
    return np.array([ x/tracks.shape[0] for x in bulk_sum])

def categorize():
    avgs = get_avg_mood_vec()
    cur_max = (0,0)
    for index,vec in enumerate(basis_mood_vecs()):
        prod = np.dot(avgs,vec)
        print(prod,vec)
        if prod > cur_max[0]:
            cur_max = (prod,vec)
    return cur_max
if __name__ == '__main__':
    for x in sp.get_top_tracks_features():
        print(x)
    print(categorize())
    

