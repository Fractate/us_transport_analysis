
import pandas as pd
import geopandas as gpd


def aggregate_join_nyc_to_buffered_networkx_stations(new_column_suffix, nyc_gdf, networkx_df, meters):
    
    networkx_gdf = gpd.GeoDataFrame(
        networkx_df,
        geometry=gpd.points_from_xy(networkx_df.stop_lon, networkx_df.stop_lat)
    )
    networkx_gdf.geometry = networkx_gdf.buffer(meters/100000)

    # Spatially join the two GeoDataFrames and aggregate the values of the 'column_to_summarize_1' and 'column_to_summarize_2' columns
    joined_mean_df = gpd.sjoin(nyc_gdf, networkx_gdf, how='left', op='intersects')\
        .groupby(['GEOID'])[['dgrs', 'clse', 'btwn']].mean().reset_index()\
        .rename(columns={'dgrs': 'dgrs_mean'+new_column_suffix})\
        .rename(columns={'clse': 'clse_mean'+new_column_suffix})\
        .rename(columns={'btwn': 'btwn_mean'+new_column_suffix})
    
    joined_sum_df = gpd.sjoin(nyc_gdf, networkx_gdf, how='left', op='intersects')\
        .groupby(['GEOID'])[['dgrs', 'clse', 'btwn']].sum().reset_index()\
        .rename(columns={'dgrs': 'dgrs_sum'+new_column_suffix})\
        .rename(columns={'clse': 'clse_sum'+new_column_suffix})\
        .rename(columns={'btwn': 'btwn_sum'+new_column_suffix})

    # Merge joined_gdf and networkx_gdf_buffered on GEOID
    joined_df = pd.merge(nyc_gdf, joined_mean_df, on='GEOID')
    joined_df = pd.merge(joined_df, joined_sum_df, on='GEOID')
    joined_gdf = gpd.GeoDataFrame(joined_df, geometry='geometry')

    return joined_gdf