import fiona
import fiona.crs
from shapely.geometry import Polygon, mapping
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import os

# Open bounding box layer (clipping layer)
def clip_shp():
    bb_path = 'data/bounding_box/uelzen/'
    bbox_polygon = []
    shp_name = []

    for file_name in [file for file in os.listdir(bb_path) if file.endswith('.shp')]:
        shape_name, _ = os.path.splitext(file_name) 
        shp_name.append(shape_name)
        aoi = fiona.open(bb_path+file_name)
        aoiGeom = Polygon(aoi[0]['geometry']['coordinates'][0])
        bbox_polygon.append(aoiGeom) 
    print(shp_name)

    # Open building layer
    shp_path = 'data/downloaded_data/shapefile/uelzen/'
    for file_name in [file for file in os.listdir(shp_path) if file.endswith('.shp')]:
        building = fiona.open(shp_path+file_name) 

    polyList = []
    polyProperties = []
    for poly in building:
        polyGeom = Polygon(poly['geometry']['coordinates'][0]) 
        polyList.append(polyGeom) 
        polyProperties.append(poly['properties'])

    for i in range(len(bbox_polygon)):
        clipPolyList = []
        clipPolyProperties = []
        for index, poly in enumerate(polyList):
                result = bbox_polygon[i].intersection(poly) 
                #print(result)
                if result.area:
                    clipPolyList.append(result)
                    clipPolyProperties.append(polyProperties[index])

        #export clipped polygons as shapefile
        ''' This has to be placed here otherwise saves for each polygon! '''
        schema = building.schema

        outFile = fiona.open('data/shp_name/uelzen/{}.shp'.format(shp_name[i]),mode = 'w',driver = 'ESRI Shapefile', crs=fiona.crs.from_epsg(25832), schema=schema)
        for index, poly in enumerate(clipPolyList):
            outFile.write({
                'geometry':mapping(poly),
                'properties':clipPolyProperties[index]
            })
        outFile.close()

def main():
    bounding = clip_shp()
    
if __name__ == "__main__":
    main() 
