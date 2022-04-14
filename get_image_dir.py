''' Utilities: helping functions that are used in one or many of the scripts '''

from osgeo import gdal
import os

def get_dir(path):
    folder = os.listdir(path) 
    path_to_name = []
    name = []

    cities = []

    for i in range(len(folder)):
        city_name = folder[i]
        #print(city_name)
        cities.append(city_name)
        city_fold = os.path.join(path, folder[i])
        image_path_indi = []
        image_name_indi = []
        for file_name in os.listdir(city_fold):
            #print(file_name)
            img_name, _ = os.path.splitext(file_name) # get .tif extension out of file name
            #print(img_name) # bad_610_5854
            image_name_indi.append(img_name)
            im = os.path.join(city_fold,file_name)
            image_path_indi.append(im)
        name.append(image_name_indi)
        path_to_name.append(image_path_indi)
        
    #print('city! : ',cities)
    #print(name, path_to_name, cities)
    return (name, path_to_name, cities)

def main():
    bounding = get_dir('data/tif') 
    
if __name__ == "__main__":
    main() 
