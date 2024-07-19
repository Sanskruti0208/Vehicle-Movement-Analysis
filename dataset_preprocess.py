# Module: data_preprocess.py
import os
import matplotlib.pyplot as plt
import numpy as np
from dataset_load import load_metadata
import pandas as pd
import cv2

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    
    # Load image using matplotlib
    image = plt.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image {image_path}.")

    # Resize image
    resized_image = cv2.resize(image, (640, 480))  # Use cv2.resize for resizing
    
    # Convert to grayscale
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

if __name__ == "__main__":
    data_dir = "C:/Users/sansk/Downloads/final/Vehicle-Movement-Analysis/data/vehicle_images"
    metadata = load_metadata(data_dir)
    
    if not metadata.empty:
        image_path = metadata.iloc[0]['vehicle_image_path']
        print(f"Loading image from path: {image_path}")  # Debug output
        try:
            preprocessed_image = preprocess_image(image_path)
            
            plt.imshow(preprocessed_image, cmap='gray')
            plt.title('Preprocessed Image')
            plt.axis('off')
            plt.show()
        except FileNotFoundError as e:
            print(e)
    else:
        print("No metadata found.")
