from src.data_reader import read_boulder_polygons, read_bathymetric_data
from src.data_processor import calculate_boulder_centroids, calculate_boulder_dimensions
from src.result_calculator import calculate_final_results
from pathlib import Path


def main():
    # Получение пути к корневой директории проекта
    project_dir = Path(__file__).parent

    # Формирование пути к файлу SHP и к файлу батиметрических данных
    shp_path = project_dir / "data/input/Test_Manually_Picked_Boulders.shp"
    bathymetry_data_path = project_dir / "data/input/Test_Encoded_Depths_File.tif"

    # Чтение данных о валунах
    boulder_polygons = read_boulder_polygons(shp_path)

    # Вычисление центроидов и размеров валунов
    centroids = calculate_boulder_centroids(shp_path)
    dimensions = [calculate_boulder_dimensions(polygon, bathymetry_data_path) for polygon in boulder_polygons.geometry]

    # Получение итоговых результатов
    final_results = calculate_final_results(boulder_polygons, centroids, dimensions)

    # Сохранение результатов
    output_path = project_dir / "data/output/output.shp"
    final_results.to_file(output_path)


if __name__ == "__main__":
    main()
