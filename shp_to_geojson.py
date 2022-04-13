import geopandas
import os

def shp_to_gjson():
    shp_path = 'data/shp_name/bremervoerde/'
    
    for file_name in [file for file in os.listdir(shp_path) if file.endswith('.shp')]:
        shape_name, _ = os.path.splitext(file_name)
        print(shape_name)
        
        shpfile = geopandas.read_file(os.path.join(shp_path,file_name))
        shpfile.to_file('data/geojson/bremervoerde/{}.geojson'.format(shape_name), driver='GeoJSON', encoding='utf-8')
        
def main():
    geojson = shp_to_gjson()
    
if __name__ == "__main__":
    main()   
