
# polygon to binary mask

import cv2
from PIL import Image
from matplotlib.pyplot import plot as plt
import numpy as np
from coordinate_extraction import polygon_extraction
import time

shape= (10000,10000)
im = np.zeros(shape)
polygon = polygon_extraction()
#print(polygon[0])
    
def poly_to_binary_mask(polygon):
    start = time.time()
    for i in range(len(polygon)): 
        print(i)
        #for j in range(len(polygon[i])): 
        poly = np.array(polygon[i]) # needs to be an array
        #print(poly)
        cv2.fillPoly(im, pts = [poly], color = (255))
        image = Image.fromarray(im)
    image.save(r'data/binary_mask/lueneburg/lueneburg17.tif') # .format(count))
    end = time.time()
    print('Time taken',(end-start)/60)
    
def main():
    binary = poly_to_binary_mask(polygon)
    
if __name__ == "__main__":
    main()
