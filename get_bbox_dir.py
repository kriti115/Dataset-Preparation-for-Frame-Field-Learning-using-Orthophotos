''' Utilities: helping functions that are used in one or many of the scripts '''

#from osgeo import gdal
import os

def get_dir(path):
    fold = os.listdir(path) # each city
    folder = sorted(fold)
    #print('City folder names', folder)
    path_to_name = []
    name = []
    cities = []

    for i in range(len(folder)):
        city_fold = os.path.join(path, folder[i]) # now inside each city folder, path to shapefiles
        #print(city_fold) # sorted
        image_path_indi = []
        image_name_indi = []
        
        shp_file_name = []
        for file in os.listdir(city_fold):
            if file.endswith('.shp'):
                shp_file_name.append(file)
        file_name = sorted(shp_file_name) # For the right order of each file inside city folder
        #print(file_name)
        for i in range(len(file_name)):
            img_name, _ = os.path.splitext(file_name[i]) 
            image_name_indi.append(img_name)
            im = os.path.join(city_fold,file_name[i])
            image_path_indi.append(im)
        name.append(image_name_indi)
        path_to_name.append(image_path_indi)

    #print('\n', name, '\n','\n', path_to_name, '\n')
    return (name, path_to_name) 

def main():
    bounding = get_dir('data/bounding_box')
    
if __name__ == "__main__":
    main() 
