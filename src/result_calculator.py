import geopandas as gpd
from shapely.geometry import Point
from typing import List


def calculate_final_results(boulder_polygons: gpd.GeoDataFrame, centroids: gpd.GeoSeries, dimensions: List[tuple]) \
        -> gpd.GeoDataFrame:
    """
    Combines the centroids and dimensions of boulders into a single GeoDataFrame with additional attributes.

    This function creates a new GeoDataFrame, setting the active geometry column to 'geometry'.
    It then adds the dimensions (length, width, height) for each boulder and includes additional attributes.

    Args:
    - boulder_polygons (gpd.GeoDataFrame): GeoDataFrame containing the original boulder polygons.
    - centroids (gpd.GeoSeries): GeoSeries containing the centroids of each boulder.
    - dimensions (List[tuple]): List of tuples representing the dimensions (length, width, height) of each boulder.

    Returns:
    - gpd.GeoDataFrame: A GeoDataFrame combining the centroids and dimensions of the boulders with additional attributes.
    """
    # Create a new GeoDataFrame for the results with the active geometry column 'geometry'
    results_gdf = gpd.GeoDataFrame(geometry=centroids)

    # Adding dimensions
    results_gdf['length'] = [dim[0] for dim in dimensions]
    results_gdf['width'] = [dim[1] for dim in dimensions]
    results_gdf['height'] = [dim[2] for dim in dimensions]

    # Adding additional attributes (e.g., Poly_ID)
    results_gdf['Poly_ID'] = boulder_polygons.index

    return results_gdf
