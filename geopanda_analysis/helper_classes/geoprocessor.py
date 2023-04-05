
import pandas as pd
import geopandas as gpd


def aggregate_join_nyc_to_buffered_networkx_stations(new_column_suffix, nyc_gdf, networkx_df, kilometers):
    
    networkx_gdf = gpd.GeoDataFrame(
        networkx_df,
        geometry=gpd.points_from_xy(networkx_df.stop_lon, networkx_df.stop_lat)
    )
    networkx_gdf.geometry = networkx_gdf.buffer(kilometers/100000)

    # Spatially join the two GeoDataFrames and aggregate the values of the 'column_to_summarize_1' and 'column_to_summarize_2' columns
    joined_df = gpd.sjoin(nyc_gdf, networkx_gdf, how='left', op='intersects')\
        .groupby(['GEOID'])[['dgrs', 'clse', 'btwn']].mean().reset_index()
    # joined_gdf = gpd.sjoin(nyc_gdf, networkx_gdf, how='inner', op='intersects')\
    #     .groupby(['GEOID'])[['dgrs', 'clse', 'btwn']].sum().reset_index()

    # Merge joined_gdf and networkx_gdf_buffered on GEOID
    joined_df = pd.merge(nyc_gdf, joined_df, on='GEOID')
    joined_gdf = gpd.GeoDataFrame(joined_df, geometry='geometry')

    joined_gdf = joined_gdf.rename(columns={'dgrs': 'dgrs'+new_column_suffix})\
        .rename(columns={'clse': 'clse'+new_column_suffix})\
        .rename(columns={'btwn': 'btwn'+new_column_suffix})

    return joined_gdf