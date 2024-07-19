import os
import pandas as pd
import cv2
from matplotlib import pyplot as plt

def load_metadata(data_dir):
    records = []
    for filename in os.listdir(data_dir):
        if filename.endswith("_metadata.txt"):
            with open(os.path.join(data_dir, filename), 'r') as f:
                metadata = {}
                for line in f:
                    try:
                        key, value = line.strip().split(": ")
                        metadata[key.strip()] = value.strip()
                    except ValueError:
                        continue  # Handle lines that don't split correctly

                if 'vehicle_timestamp' in metadata:
                    try:
                        # Adjust the format string to match the timestamp format in the metadata files
                        metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'], format="%Y-%m-%d %H:%M:%S")
                        records.append(metadata)
                    except ValueError as e:
                        print(f"Error parsing timestamp in file: {filename}, error: {e}")
                        print(f"Invalid timestamp: {metadata['vehicle_timestamp']}")
                else:
                    print(f"Warning: 'vehicle_timestamp' not found in file: {filename}")

    if not records:
        print("No valid metadata found.")
    else:
        print(f"Loaded metadata for {len(records)} files.")
    
    return pd.DataFrame(records)

def display_sample_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Failed to load image {image_path}.")
        return

    # Convert BGR image to RGB for displaying with Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title('Sample Image')
    plt.axis('off')  # Hide axis
    plt.show()

# Usage
if __name__ == "__main__":
    data_dir = r"C://Users//sansk//Downloads//final//Vehicle-Movement-Analysis//data//vehicle_images"
    metadata = load_metadata(data_dir)
    
    if not metadata.empty:
        print(metadata.head())
        # Assuming vehicle_image_path is part of the metadata DataFrame
        display_sample_image(metadata.iloc[0]['vehicle_image_path'])
    else:
        print("No metadata found.")
