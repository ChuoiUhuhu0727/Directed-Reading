# Practice: Cleaning Sensor data 

This exercise shows basic data-cleaning steps on synthetic sensor data, focusing on handling missing values and visualizing data distribution before-and-after cleaning. 

## Contents
- `sensor_data_cleaning.py`: Python code to generate, analyze, clean and visualize sensor data
- `humidity_before_cleaning.png`, `humidity_after_cleaning.png`, `temp_before_cleaning.png`, `temp_after_cleaning.png`: images of data before and after cleaning. Humidity and Temperature are 2 main scales of this dataset

## Data Generation
- **Sensors:** 5 simulated sensors (`sensor_id` 1–5)
- **Features:** Each row includes a timestamp, sensor ID, temperature, humidity, and location.
- **Missing Data:** 3 columns (humidity, temperature, location) have random missing values

## Data Cleaning
- **Missing Analysis:** The code analyzes whether there are patterns of missing values and makes use of data grouping to fill in.
- **Filling Strategies:**
  -  **Forward and backward fill:** for each sensor_id, missing values are filled by last known value (forward fill) and next known value (backward fill).
  -   **Interpolation:**: use if this is a large dataset
  -   **Mapping:** use mapping methods to match missing values with most suitable values

## Usage 
1. **Run the script:**
  The code is in `sensor_data_cleaning`.
  Make sure you have the required libraries:
  ```sh
   pip install pandas numpy matplotlib
   ```
   Then run:
   ```sh
   python clean_data1.py
   ```

2. **View the generated images:**
  The code genrates 4 plots.
  The included `.png` files are example outputs.

## Learning Points
- Get accustomed to 1 out of 4 most popular data-missing scenerios (missing with patterns)
- Practice data-filling techinques:
    - mapping, backfill, forward fill: for small dataset
    - interpolation: for large dataset
- Visulize and compare data before and after cleaning
