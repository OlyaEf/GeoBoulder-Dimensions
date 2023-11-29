import geopandas as gpd
import sys
from pathlib import Path

# Retrieving the path to the project directory (Получение пути к директории проекта)
project_dir = Path(__file__).parent.parent

# Adding the path to the src directory in sys.path (Добавление пути к директории src в sys.path)
sys.path.append(str(project_dir / "src"))

from src.data_processor import calculate_boulder_dimensions

# Paths to the test data  (Пути к тестовым данным)
shp_path = project_dir / "data/input/Test_Manually_Picked_Boulders.shp"
bathymetry_data_path = project_dir / "data/input/Test_Encoded_Depths_File.tif"

boulder_polygons = gpd.read_file(shp_path)
for polygon in boulder_polygons.geometry:
    length, width, height = calculate_boulder_dimensions(polygon, bathymetry_data_path)
    if __name__ == "__main__":
        print(f"Length: {length}, Width: {width}, Height: {height}")
