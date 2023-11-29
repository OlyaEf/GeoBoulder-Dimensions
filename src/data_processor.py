import geopandas as gpd
import numpy as np
import rasterio

from pathlib import Path
from geopandas import GeoSeries
from shapely.geometry import Polygon
from typing import Tuple, Union


def calculate_boulder_centroids(shp_path: Path) -> GeoSeries:
    """
    Calculates the centroids of each boulder represented as a polygon in a SHP file.

    This function takes a path to a SHP file, reads the polygon geometries representing
    boulders, and calculates the centroid for each polygon. The centroids represent the
    geometric center point of the boulders.

    Parameters:
    - shp_path (Path): Path to the SHP file containing boulder polygons.

    Returns:
    - gpd.GeoSeries: A GeoSeries containing the centroids of each boulder polygon.
    """

    # Load boulder polygons from the SHP file
    boulder_polygons = gpd.read_file(shp_path)

    # Calculate centroids for each polygon
    boulder_centroids = boulder_polygons.geometry.centroid

    # Create a new GeoDataFrame with centroids
    gpd.GeoDataFrame(geometry=boulder_centroids)

    # Calculate and return centroids for each polygon
    return boulder_polygons.geometry.centroid


def calculate_boulder_dimensions(boulder_polygon: Polygon, bathymetry_data_path: Union[str, Path]) -> Tuple[float, float, float]:
    """
    Calculates the length, width, and height dimensions of a boulder based on its polygon
    representation and bathymetric data.

    The function computes the length and width of the boulder by determining the maximum
    extents of the polygon. The height is calculated using bathymetric data, which provides
    the elevation difference between the seabed and the highest point of the boulder.

    Args:
    - boulder_polygon (Polygon): The polygon representing the boulder.
    - bathymetry_data_path (Union[str, Path]): Path to the GeoTiff file containing bathymetric data.

    Returns:
    - Tuple[float, float, float]: A tuple containing the length, width, and height of the boulder in meters.
    """

    # Calculate length and width based on polygon bounds
    bounds = boulder_polygon.bounds
    length = bounds[2] - bounds[0]  # maxx - minx
    width = bounds[3] - bounds[1]  # maxy - miny

    # Load bathymetric data for height calculation
    with rasterio.open(bathymetry_data_path) as src:
        bathymetry = src.read(1)  # Reading the first channel
        transform = src.transform

        # Convert polygon coordinates to raster indices
        raster_indices = [~transform * (x, y) for x, y in boulder_polygon.exterior.coords]
        row_indices, col_indices = zip(*raster_indices)

        # Extract elevation data within the polygon
        boulder_heights = bathymetry[np.round(row_indices).astype(int), np.round(col_indices).astype(int)]
        seabed_height = np.min(boulder_heights)  # Assuming seabed height is the minimum around the boulder
        boulder_top_height = np.max(boulder_heights)  # Assuming top height is the maximum within the polygon

        # Calculate height as the difference between the seabed and the boulder's top
        height = boulder_top_height - seabed_height

    return length, width, height
