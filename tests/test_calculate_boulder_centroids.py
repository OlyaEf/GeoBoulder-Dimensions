import unittest
import geopandas as gpd


from pathlib import Path
from src.data_processor import calculate_boulder_centroids

# Retrieving the path to the project directory (Получение пути к директории проекта)
project_dir = Path(__file__).parent.parent
# Path to the test data (Путь к тестовым данным)
shp_path = project_dir / "data/input/Test_Manually_Picked_Boulders.shp"


class TestCalculateBoulderCentroids(unittest.TestCase):
    def test_boulder_centroids(self):

        # Call the function to calculate centroids (Вызов функции для вычисления центроидов)
        centroids = calculate_boulder_centroids(shp_path)

        # Expected number of centroids (Ожидаемое количество центроидов)
        boulder_polygons = gpd.read_file(shp_path)
        expected_number_of_centroids = len(boulder_polygons)

        # Check that the result is not empty (Проверка, что результат не пустой)
        self.assertTrue(not centroids.empty)

        # Check the number of centroids (Проверка количества центроидов)
        self.assertEqual(len(centroids), expected_number_of_centroids)

    def test_return_type(self):
        # Check the type of the returned object
        centroids = calculate_boulder_centroids(shp_path)
        self.assertIsInstance(centroids, gpd.GeoSeries)

    def test_centroid_geometry(self):
        # Check that the returned objects are centroids (Проверка, что возвращаемые объекты являются центроидами)
        boulder_polygons = gpd.read_file(shp_path)
        centroids = calculate_boulder_centroids(shp_path)
        for original, centroid in zip(boulder_polygons.geometry, centroids.geometry):
            self.assertTrue(original.contains(centroid) or original.touches(centroid))


if __name__ == "__main__":
    unittest.main()
