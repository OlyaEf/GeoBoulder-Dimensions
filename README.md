# GeoBoulder-Dimensions

## Project Description
GeoBoulder-Dimensions is a Python script designed for automatically measuring three key 
dimensions (length, width, and height) of seabed boulders based on Multibeam Echo Sounder 
(MBES) data. The script utilizes SHP format vector data to outline boulders and GeoTiff format 
raster data for bathymetric values. The processing results are saved in an SHP file compatible 
with QGIS 3.28 software.

## Methodology
The script follows a straightforward methodology:
1. **Reading Data**: It begins by reading the vector layer (SHP format) containing 
polygons that approximate the shape of the boulders and a gridded surface of bathymetric 
average values (GeoTiff format).
2. **Calculating Centroids and Dimensions**: The script then calculates the centroids for 
each boulder polygon. It also measures the three key dimensions (length, width, and height) 
for each boulder.
3. **Combining Results**: The final step involves combining these measurements into a single 
output vector layer (SHP format) with detailed attribute fields.

## Technologies
- Python 3.11
- GeoPandas
- Rasterio
- Fiona
- Shapely

## Project Structure
GeoBoulder-Dimensions/
│
├── data/
│ ├── input/
│ │ ├── Test_Encoded_Depths_File.tif
│ │ └── Test_Manually_Picked_Boulders.shp
│ └── output/
│ └── output.shp
│
├── src/
│ ├── init.py
│ ├── data_processor.py
│ ├── data_reader.py
│ └── result_calculator.py
│
├── tests/
│ ├── init.py
│ ├── test_calculate_boulder_centroids.py
│ ├── test_calculate_boulder_dimensions.py
│ ├── test_data_reader.py
│ └── test_result_calculator.py
│
├── main.py
├── poetry.lock
└── pyproject.toml


## Installation and Running
Python 3.11 and installed dependencies are required for the project. 
It is recommended to use the Poetry package manager to manage dependencies.

### Cloning the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/OlyaEf/GeoBoulder-Dimensions.git
   cd GeoBoulder-Dimensions
   ```


### Installing Dependencies
2. Install dependencies:
    ```bash
    poetry install
    ```


### Activating the Virtual Environment
3. Activate the Poetry virtual environment:
   ```bash
    poetry shell
    ```


### Running the Script
4. Run the main script:
   ```bash
   python main.py
   ```

## Usage
1. Place SHP and GeoTiff files with boulder and bathymetric data in the `data/input/` folder.
2. Run `main.py` to process the data and generate the final SHP file in the `data/output/` folder.
3. The final file can be opened and analyzed in QGIS 3.28.

## Testing
To test the script, navigate to the `tests` directory and run the test files using a Python test runner. 
These tests validate various functionalities of the script such as reading data, calculating centroids and 
dimensions, and generating the final output.

Run tests via command in the activated Poetry environment:
   ```bash
   python -m unittest
   ```

## Output Format
The output of the script is a SHP file containing:
- Points approximating the centroids of input boulder polygons.
- Each point includes the following attributes:
- `Poly_ID`: Polygon ID from the input data.
- `Target ID`: Includes "MBES" value, block name, and target order number.
- `Block`: User-provided value in the script settings.
- `Easting`, `Northing`: Coordinates of the boulder centroid.
- `Water depth`: Water depth at the boulder centroid location.
- `Length`, `Width`, `Height`: Dimensions of the boulder in meters.

The output layer is stored in the same folder as the input vector layer.

## Compatibility with QGIS 3.28
This script is compatible with QGIS 3.28. Users can import the output SHP file into 
QGIS to visualize and further analyze the data.

## Additional Documentation
For a detailed explanation of the methodology and procedures used in the creation of 
this script, please refer to the accompanying Word document [Ссылка на документацию](/home/OlyaEf/SkyproProjects/GeoBoulder-Dimensions/dock.word).


## Authors
Olya Efimovskikh (https://github.com/OlyaEf)
