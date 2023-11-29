from src.data_reader import read_boulder_polygons, read_bathymetric_data
from pathlib import Path

# Get the path to the directory where the current script is located
current_dir = Path(__file__).parent


def test_read_boulder_polygons():
    shp_path = current_dir / "../data/input/Test_Manually_Picked_Boulders.shp"
    boulder_polygons = read_boulder_polygons(shp_path)
    print(boulder_polygons.head())  # Print the first few lines of the GeoDataFrame (Вывод 1-ых нескольких строк)


def test_read_bathymetric_data():
    tif_path = current_dir / "../data/input/Test_Encoded_Depths_File.tif"
    bathymetry, transform = read_bathymetric_data(tif_path)
    print(bathymetry)  # Print the bathymetry data array (Вывод массива данных о батиметрии)
    print(transform)   # Print the transformation for the GeoTiff file (Вывод преобразования для GeoTiff файла)


if __name__ == "__main__":
    test_read_boulder_polygons()
    test_read_bathymetric_data()
