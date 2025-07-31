# PRACTICE CLEANING DATA
# Exercise 1: 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
num_rows = 100
num_sensors = 5
start_time = pd.Timestamp('2025-01-01 00:00:00')

# Generate timestamps (hourly readings)
timestamps = [start_time + pd.Timedelta(hours=i) for i in range(num_rows)]

# Assign sensor IDs randomly
sensor_ids = np.random.choice(range(1, num_sensors + 1), size=num_rows)

# Simulate temperature and humidity readings
temperatures = np.random.normal(loc=22, scale=3, size=num_rows)
humidity = np.random.normal(loc=50, scale=10, size=num_rows)

# Introduce missing temperature and humidity (simulate sensor malfunction)
missing_temp_idx = np.random.choice(num_rows, size=10, replace=False)
missing_hum_idx = np.random.choice(num_rows, size=8, replace=False)
temperatures[missing_temp_idx] = np.nan
humidity[missing_hum_idx] = np.nan

# Assign locations per sensor ID, with some missing locations for new sensors
location_map = {1: "Lab A", 2: "Lab B", 3: "Greenhouse", 4: None, 5: "Warehouse"}
locations = [location_map[sid] for sid in sensor_ids]

# For illustration, let's make 5 more locations missing at random
random_missing_idx = np.random.choice(num_rows, size=5, replace=False)
for idx in random_missing_idx:
    locations[idx] = None

# Build DataFrame
sensor_data = pd.DataFrame({
    'timestamp': timestamps,
    'sensor_id': sensor_ids,
    'temperature': temperatures,
    'humidity': humidity,
    'location': locations
})

# Save to CSV for practice
sensor_data.to_csv('sensor_data.csv', index=False)

# Show a preview
print(sensor_data.head(10))

# Preview data 
sensor_data['temperature'].isna().unique()
sensor_data['temperature'].unique()
sensor_data['sensor_id'].unique()
sensor_data[sensor_data['temperature'].isna()]['sensor_id'].unique()

# Pattern: Only sensor_id 3 doesnt lose 
# data about temperature 
sensor_data[sensor_data['temperature'].isna()].head()
sensor_data[sensor_data['sensor_id'] == 2]
sensor_data[sensor_data['sensor_id'] == 1]
sensor_data['humidity'].unique()
sensor_data[sensor_data['humidity'].isna()]['sensor_id'].unique()

# Goal 1: Analyze the pattern of missing values in sensor_data
# Goal 2: Clean/Handle the missing data as appropriate for further analysis.

# Way 1: customised for this dataset
# Sort by sensor_id and timestamp 
sensor_filled = (
    sensor_data
    .sort_values(['sensor_id', 'timestamp'])
    .groupby('sensor_id')
    .apply(lambda df: df.ffill().bfill())
    .reset_index(drop=True)
)
sensor_filled

# Way 2: for large dataset
# Use interpolate
sensor_inter = sensor_data.groupby('sensor_id').apply(
    lambda df: df.interpolate(limit_direction='both')
)
sensor_inter

# Recheck null columns
sensor_filled.isnull().any()
sensor_inter.isnull().any()

# Handdle missing location
location_map = (
    sensor_filled.dropna(subset='location')
    .drop_duplicates(subset='sensor_id')
    .set_index('sensor_id')['location']
    .to_dict()
)
sensor_filled['location'] = sensor_filled['sensor_id'].map(location_map)

# Visualize dataset before 
# and after filling
sensor_id_to_plot = 1

# Before filling Temperature
original_data = sensor_data[sensor_data['sensor_id'] == sensor_id_to_plot]
plt.figure(figsize=(12,4))
plt.plot(original_data['timestamp'], original_data['temperature'], 'o-', label='Original (with NaNs)')
plt.title(f'Sensor {sensor_id_to_plot} Temperature Before Filling')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# After filling Temperature
sensor_filled['temperature'] = sensor_filled.groupby('sensor_id')['temperature'].ffill()
sensor_filled = sensor_filled[sensor_filled['sensor_id'] == sensor_id_to_plot]
plt.figure(figsize=(12,4))
plt.plot(sensor_filled['timestamp'], sensor_filled['temperature'], 'o-', label='After Filling')
plt.title(f'Sensor {sensor_id_to_plot} Temperature After Filling')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# Before filling Humidity
original_data = sensor_data[sensor_data['sensor_id'] == sensor_id_to_plot]
plt.figure(figsize=(12,4))
plt.plot(original_data['timestamp'], original_data['humidity'], 'o-', label='Original (with NaNs)')
plt.title(f'Sensor {sensor_id_to_plot} Humidity Before Filling')
plt.xlabel('Timestamp')
plt.ylabel('Humidity')
plt.legend()
plt.show()

# After filling Humidity
sensor_filled['humidity'] = sensor_filled.groupby('sensor_id')['humidity'].ffill()
sensor_filled = sensor_filled[sensor_filled['sensor_id'] == sensor_id_to_plot]
plt.figure(figsize=(12,4))
plt.plot(sensor_filled['timestamp'], sensor_filled['humidity'], 'o-', label='After Filling')
plt.title(f'Sensor {sensor_id_to_plot} Humidity After Filling')
plt.xlabel('Timestamp')
plt.ylabel('Humidity')
plt.legend()
plt.show()
