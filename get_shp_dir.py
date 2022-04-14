''' Utilities: helping functions that are used in one or many of the scripts '''

#from osgeo import gdal
import os

def get_dir_shp(path_shp):
    fold = os.listdir(path_shp) 
    folder = sorted(fold)
    path_to_name = []
    name_shp = []
    cities = []

    for i in range(len(folder)):
        city_name = folder[i]
        cities.append(city_name)
        city_fold = os.path.join(path_shp, folder[i])
        for file_name in os.listdir(city_fold):
            if file_name.endswith('.shp'):
                img_name, _ = os.path.splitext(file_name)
                im = os.path.join(city_fold,file_name)
                path_to_name.append(im)
                name_shp.append(img_name)

    #print(name_shp, path_to_name)
    return name_shp, path_to_name

def main():
    bounding = get_dir_shp('data/shapefile')
    
if __name__ == "__main__":
    main()  
