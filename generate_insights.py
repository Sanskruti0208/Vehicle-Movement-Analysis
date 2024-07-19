import tkinter as tk
from tkinter import ttk
import pandas as pd
from dataset_load import load_metadata  

def generate_insights(metadata):
    
    metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'])
    
    # Example insights
    vehicle_entry_exit_times = metadata[['vehicle_image_path', 'vehicle_timestamp']]
    
    # Calculate average parking occupancy by hour
    if not metadata.empty:
        metadata['hour'] = metadata['vehicle_timestamp'].dt.hour
        avg_parking_occupancy = metadata['hour'].value_counts().mean()
    else:
        avg_parking_occupancy = 0
    
    insights = {
        "Vehicle Entry and Exit Times": vehicle_entry_exit_times,
        "Average Parking Occupancy": avg_parking_occupancy
    }
    
    return insights

def show_insights():
    # Corrected data directory path
    data_dir = "C:/Users/sansk/Downloads/final/Vehicle-Movement-Analysis/data/vehicle_images"
    
    # Load metadata
    metadata = load_metadata(data_dir)
    
    if not metadata.empty:
        insights = generate_insights(metadata)
        
        # Create a Tkinter window
        window = tk.Tk()
        window.title("Vehicle Movement Insights")
        
        # Create a label for each insight
        for idx, (key, value) in enumerate(insights.items()):
            if isinstance(value, pd.DataFrame):
                label_text = f"{key}: \n{value.to_string(index=False)}"
            else:
                label_text = f"{key}: {value}"
            
            label = ttk.Label(window, text=label_text, wraplength=400, justify="left")
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
        
        # Start the Tkinter main loop
        window.mainloop()
    else:
        print("No metadata found.")

if __name__ == "__main__":
    show_insights()
