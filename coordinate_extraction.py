# image coordinate extraction from geojson

import json
import numpy as np
import cv2
import matplotlib.pyplot as plt 

from osgeo import gdal, ogr

from PIL import Image

def polygon_extraction():
    #with open('data/geojson/395_5707_rad.geojson', 'r',  encoding="utf8" ) as f:
    with open('data/geojson/lueneburg/lueneburg14.geojson', 'r',  encoding="utf8" ) as f:
        data = json.loads(f.read())

        ''' Extract coordinates for each polygon '''

    coord = []
    #print(len(data['features']))
    for i in range(len(data['features'])):
        coo = data['features'][i]['geometry']['coordinates']
        #print(coord, '\n')
        coord.append(coo)
        
    coordinates = []
    for i in range(len(coord)): # 2099
        if len(coord[i]) == 1:
            for j in range(len(coord[i])):
                c = coord[i][j]
                coordinates.append(c)
        else:
            for j in range(len(coord[i])):
                #print(j)
                for k in range(len(coord[j])): 
                    c = coord[i][j][k]
                    coordinates.append(c)
    print(len(coordinates), '\n')
#     print(coordinates[0], '\n')
#     print(coordinates[0][0], '\n')
    #print(coordinates[0][0][0], '\n')


    ''' Get minimum and maximum coordinates '''
    def get_coor_in_space(image_filepath):
        ds = gdal.Open(image_filepath)
        width = ds.RasterXSize
        height = ds.RasterYSize
        gt = ds.GetGeoTransform()

        x_min = gt[0]
        y_min = gt[3] + width * gt[4] + height * gt[5]
        x_max = gt[0] + width * gt[1] + height * gt[2]
        y_max = gt[3]

        return x_min, y_min
    
    ''' Convert to pixel coordinates '''
    #image_filepath = 'data/tif/395_5707.tif'
    image_filepath = 'data/downloaded_data/images/lueneburg/lueneburg14.tif'
    x_min =  get_coor_in_space(image_filepath)[0]
    y_min =  get_coor_in_space(image_filepath)[1]
    #print(x_min, y_min)

    polygon = []
    for i in range (len(coordinates)):
        #print(i)
        x_pixel = []
        y_pixel = []
        for j in range(len(coordinates[i])):
            #print(j)
            x_pix =  int((coordinates[i][j][0]-x_min)*5) # scaling = 10000/2000 = 5 i.e. image size/pixel size
            y_pix =  int(10000 - ((coordinates[i][j][1]-y_min)*5)) 
          
            x_pixel.append(x_pix)
            y_pixel.append(y_pix)
        #print('x_pixel:', x_pixel, '\n', 'y_pixel: ',y_pixel, ' \n')

        row, col = (len(x_pixel),2)
        pixel = [[0]*col for y in range(row)]
        for i in range(len(x_pixel)):
            pixel[i][0] = x_pixel[i]
            pixel[i][1] = y_pixel[i]
        polygon.append(pixel)
    #print(polygon)

    return polygon

def main():
    polygon = polygon_extraction()
    
if __name__ == "__main__":
    main()

