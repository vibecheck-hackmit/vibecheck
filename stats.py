import numpy as np
#using: array

import spotify as sp
#using: 

import typing as ty

import math

def basis_mood_vecs() -> ty.Tuple[np.array]:
    return (np.array([1,1,1])
           ,np.array([1,1,0])
           ,np.array([0.1,0.1,0.1]) #dont want zero vec
           ,np.array([0,1,0])
           ,np.array([1,0,1])
           ,np.array([0,0,1])
           ,np.array([0.5,0.5,0.5])
           ,np.array([1,0.5,0])
           ,np.array([0.5,1,0.5])
           ,np.array([0,0.5,1])
           )


def get_avg_mood_vec() -> np.array:

    #get top tracks and make vectors that represent mood.
    tracks = np.array([ [ x.danceability, x.energy, x.valence ] for x in sp.get_top_tracks_features() ])

    #get the sum of all rows in the matrix
    bulk_sum = tracks.sum(axis=0)
    
    #avg mood vector
    avg = np.array([ x/tracks.shape[0] for x in bulk_sum])
    norm = np.linalg.norm(avg)

    return np.array([ x/norm for x in avg])

def categorize():
    avgs = get_avg_mood_vec()
    #avgs = np.array([0.1,0.1,0.1]) #dont want zero vec
    print(avgs)
    cur_max = (float('inf'),0,0)
    for index,vec in enumerate(basis_mood_vecs()):
        prod = math.sqrt( (avgs[0]-vec[0])**2 + (avgs[1]-vec[1])**2 + (avgs[2]-vec[2])**2)
        print(prod,vec,index)
        if prod < cur_max[0]:
            cur_max = (prod,vec,index)
    return cur_max[2]
if __name__ == '__main__':
    for x in sp.get_top_tracks_features():
        print(x)
    print(categorize())
    print(get_avg_mood_vec())
    

