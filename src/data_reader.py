import geopandas as gpd
import rasterio
import numpy as np
from typing import Union, Tuple
from pathlib import Path


def read_boulder_polygons(shp_path: Union[str, Path]) -> gpd.GeoDataFrame:
    """
    Reads a shapefile containing boulder polygons and returns a GeoDataFrame.

    Args:
    shp_path (Union[str, Path]): Path to the shapefile.

    Returns:
    gpd.GeoDataFrame: GeoDataFrame containing the polygons data.
    """
    return gpd.read_file(shp_path)


def read_bathymetric_data(tif_path: Union[str, Path]) -> Tuple[np.ndarray, rasterio.Affine]:
    """
    Reads a GeoTiff file containing bathymetric data and returns the raster data and transform.

    Args:
    tif_path (Union[str, Path]): Path to the GeoTiff file.

    Returns:
    Tuple[np.ndarray, rasterio.Affine]: Tuple containing the raster data array and the affine transform.
    """
    with rasterio.open(tif_path) as src:
        bathymetry = src.read(1)  # Reading the first channel
        return bathymetry, src.transform
