''' Extracting bounding box as shapefiles with naming equivalent to the image name! AWESOME! with the directory and other utilities as function ''' 

import shapely.geometry
import pandas as pd
import geopandas as gpd
from osgeo import gdal
import os
from utils import createFolder, boundingBox
from get_image_dir import get_dir


def bb_as_shp(path_to_image):
    image_name = get_dir(path_to_image)[0]
    #print(image_name)
    image_path = get_dir(path_to_image)[1]
    cities = get_dir(path_to_image)[2]
    
    bound_box = []
    for i in range(len(image_path)):
        for j in range(len(image_path[i])):
            print(image_path[i][j])
            bb = boundingBox(image_path[i][j])
            bound_box.append(bb)
    #print(bound_box)
    
    createFolder('./data/bounding_box/')
    bb = []
    for i in range(len(image_path)): # 4
        createFolder('./data/bounding_box/{}/'.format(cities[i])) 
        for j in range(len(image_path[i])): 
            bb = shapely.geometry.box(*bound_box[i], ccw=True)
            print(bb)
            gpd.GeoDataFrame(pd.DataFrame(['p1'], columns = ['geom']),crs = {'init': 'epsg:25832'},
             geometry = [bb]).to_file('data/bounding_box/{}/{}.shp'.format(cities[i], image_name[i][j]))

def main():
    bounding = bb_as_shp('data/images')
    
if __name__ == "__main__":
    main() 
