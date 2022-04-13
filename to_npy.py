# to npy

import numpy as np
from coordinate_extraction import polygon_extraction

''' to array '''

polygon = polygon_extraction()
poly_array = np.array([np.array(i) for i in polygon])

#count = 1
for i in range(len(poly_array)):
    with open('data/npy/cuxhaven/cuxhaven7.npy', 'wb') as f: 
        np.save(f,poly_array)
