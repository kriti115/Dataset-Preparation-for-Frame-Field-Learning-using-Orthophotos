''' Utilities: helping functions that are used in one or many of the scripts '''

from osgeo import gdal
import os

def boundingBox(image_filepath):
    ds = gdal.Open(image_filepath)
    width = ds.RasterXSize
    height = ds.RasterYSize
    gt = ds.GetGeoTransform()

    x_min = gt[0]
    y_min = gt[3] + width * gt[4] + height * gt[5]
    x_max = gt[0] + width * gt[1] + height * gt[2]
    y_max = gt[3]

    return (x_min, y_min, x_max, y_max)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
