# Data retrieval will all take place in the form of dataframes for compartmentalized data conversions

import geopandas as gpd
import urllib.request
import zipfile
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Retrieve Census Tiger Shapefile
def retrieve_census_tiger_shapefile_dataframe():
        
    # Set the download URL, file name and folder path
    url = "https://www2.census.gov/geo/tiger/TIGER2019/BG/tl_2019_36_bg.zip"
    filename = "tl_2019_36_bg.zip"
    folder_path = "./data/ny_blockgroup_shapefile"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Check if the shapefile exists, otherwise download and unzip it
    if not os.path.exists(os.path.join(folder_path, "tl_2019_36_bg.shp")):
        # Download and unzip the shapefile
        urllib.request.urlretrieve(url, os.path.join(folder_path, filename))
        with zipfile.ZipFile(os.path.join(folder_path, filename), 'r') as zip_ref:
            zip_ref.extractall(folder_path)

    # Read the shapefile into a geopandas GeoDataFrame
    gdf = gpd.read_file(os.path.join(folder_path, "tl_2019_36_bg.shp"))

    # '085' for Staten Island is removed for its lack of GTFS files
    nyc_counties_fp = ['005', '047', '061', '081'] # FIPS codes for New York City counties
    nyc_gdf = gdf[gdf['COUNTYFP'].isin(nyc_counties_fp)]
    nyc_gdf = nyc_gdf.reset_index(drop=True)
    nyc_gdf['GEOID'] = nyc_gdf['GEOID'].astype('int64')

    return nyc_gdf

    
# Retrieve Presaved networkx results
def retrieve_networkx_result(file_name):

    # Read the networkx_analysis.csv file into a pandas DataFrame
    networkx_df = pd.read_csv("./data/networkx_analysis_results/"+file_name)
    # networkx_df = pd.read_csv("./data/networkx_analysis_results/networkx_analysis_with_pop.csv")

    # # Convert the networkx_df DataFrame to a geopandas GeoDataFrame and create circles around each station
    # networkx_gdf = gpd.GeoDataFrame(
    #     networkx_df,
    #     geometry=gpd.points_from_xy(networkx_df.stop_lon, networkx_df.stop_lat),
    #     crs=crs_text
    # )

    # # Create a 1km buffer around the points in networkx_gdf
    # networkx_gdf_buffered = networkx_gdf.copy()

    # # Change the CRS to the desired CRS
    # networkx_gdf_buffered = networkx_gdf_buffered.to_crs(crs_text)
    # networkx_gdf_buffered.geometry = networkx_gdf_buffered.buffer(0.03)

    # # Convert the buffered points to a GeoDataFrame
    # networkx_gdf_buffered = gpd.GeoDataFrame(networkx_gdf_buffered)
    return networkx_df

# Retrieve Presaved Social Explorer NYC Blockgroup data results
def retrieve_socialexplorer_blockgroup_data():
    return pd.read_csv('./data/socialexplorer_nyc_blockgroup_data/socialexplorer_nyc_blockgroup_data.csv', header=1, delimiter=',')


def generate_column_names():
    df = pd.read_csv('./data/socialexplorer_nyc_blockgroup_data/socialexplorer_nyc_blockgroup_data.csv', header=None, delimiter=',')
    
    # Invert the first two rows of df and store the result in a new DataFrame named column_decode
    column_decode = pd.DataFrame({'definition': df.iloc[0, :], 'key': df.iloc[1, :]})

    # Reset the index of column_decode to use integers as the index
    column_decode = column_decode.reset_index()

    # Rename the index and column names
    column_decode = column_decode.rename(columns={'index': 'feature'})

    # Export column_decode to a CSV file named "column_names.csv" in the "data" directory with only the "definition" and "key" columns
    column_decode.to_csv('./data/socialexplorer_nyc_blockgroup_data/column_names.csv', columns=['definition', 'key'], index=False)

import requests
import geopandas as gpd
import os
import shutil
import zipfile
import os
import requests
import zipfile
import geopandas as gpd
import pandas as pd

def retrieve_road_data():

    urls = [
        "https://www2.census.gov/geo/tiger/TIGER2019/ROADS/tl_2019_36005_roads.zip",
        "https://www2.census.gov/geo/tiger/TIGER2019/ROADS/tl_2019_36047_roads.zip",
        "https://www2.census.gov/geo/tiger/TIGER2019/ROADS/tl_2019_36061_roads.zip",
        "https://www2.census.gov/geo/tiger/TIGER2019/ROADS/tl_2019_36081_roads.zip"
    ]

    # create the output directory if it does not exist
    output_dir = "./data/road_shapefiles/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # download and extract shapefiles
    shapefiles = []
    for url in urls:
        filename = os.path.join(output_dir, os.path.basename(url))  # extract filename from url and join with output directory
        dirname = os.path.splitext(filename)[0]  # create directory name from filename

        # skip download if file already exists
        if os.path.exists(dirname):
            print(f"Directory {dirname} already exists, skipping extraction.")
        else:
            if os.path.exists(filename):
                print(f"File {filename} already exists, skipping download.")
            else:
                print(f"Downloading {filename}...")
                response = requests.get(url)
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"Done downloading {filename}")

            # extract shapefiles
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if file.endswith('.shp') or file.endswith('.shx') or file.endswith('.dbf'):
                        zip_ref.extract(file, dirname)

        # add shapefile path to list
        shapefile_path = os.path.join(dirname, f"tl_2019_{os.path.basename(dirname).split('_')[2]}_roads.shp")
        shapefiles.append(shapefile_path)

    # combine shapefiles into a single GeoDataFrame
    gdf = gpd.GeoDataFrame(pd.concat([gpd.read_file(shpfile) for shpfile in shapefiles], ignore_index=True), crs=gpd.read_file(shapefiles[0]).crs)

    # filter out s1100 and s1200 from MTFCC to keep roads local
    mtfcc_filter = ~gdf['MTFCC'].isin(['S1100', 'S1200'])
    gdf_filtered = gdf[mtfcc_filter]
    
    return gdf_filtered