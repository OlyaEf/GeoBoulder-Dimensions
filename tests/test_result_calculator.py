import unittest
import geopandas as gpd
from pathlib import Path
from src.data_reader import read_boulder_polygons, read_bathymetric_data
from src.data_processor import calculate_boulder_centroids, calculate_boulder_dimensions
from src.result_calculator import calculate_final_results


class TestResultCalculator(unittest.TestCase):
    def test_calculate_final_results_on_real_data(self):
        # Retrieving the absolute path to the project directory (Получение абсолютного пути к директории проекта)
        project_dir = Path(__file__).parent.parent

        # Absolute paths to the test data (Абсолютные пути к тестовым данным)
        shp_path = project_dir / "data/input/Test_Manually_Picked_Boulders.shp"
        tif_path = project_dir / "data/input/Test_Encoded_Depths_File.tif"

        # Reading the boulder data (Чтение валунов)
        boulder_polygons = read_boulder_polygons(shp_path)

        # Calculating centroids (Вычисление центроидов)
        centroids = calculate_boulder_centroids(shp_path)

        # Calculating dimensions for each boulder (Вычисление размеров каждого валуна)
        dimensions = [calculate_boulder_dimensions(polygon, tif_path) for polygon in boulder_polygons.geometry]

        # Combining results (Объединение результатов)
        final_results = calculate_final_results(boulder_polygons, centroids, dimensions)

        # Checking the type of the returned object (Проверка типа возвращаемого объекта)
        self.assertIsInstance(final_results, gpd.GeoDataFrame)

        # Checking that the number of rows matches expectations (Проверка, что количество строк совпадает с ожидаемым)
        self.assertEqual(len(final_results), len(boulder_polygons))

        # Additional checks, such as the presence of expected columns (Дополнительные проверки, например, наличие ожидаемых столбцов)
        expected_columns = ['geometry', 'length', 'width', 'height']
        for column in expected_columns:
            self.assertIn(column, final_results.columns)


if __name__ == '__main__':
    unittest.main()
