import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Add the Data_Loader folder to Python's path so we can import Day 1's code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Data_Loader')))
from EEGIS_dataset import EEGISDataset

def run_day2_visualization():
    print("=" * 60)
    print(" DAY 2: EEG SIGNAL VISUALIZATION & SANITY CHECK")
    print("=" * 60)

    # 1. Connect to Day 1's Data Loader
    dataset_dir = os.path.join("06_Implementation", "01_Data", "Raw", "EEGIS", "raw")
    
    if not os.path.exists(dataset_dir):
        print(f"[ERROR] Could not find data at: {dataset_dir}")
        return

    # Load the dataset
    dataset = EEGISDataset(root_dir=dataset_dir)
    print(f"[INFO] Dataset connected. Total files: {len(dataset)}")

    # 2. Extract exactly one file (the very first CSV)
    eeg_tensor, label = dataset[0]  # Shape is [14, 128]
    
    # Convert PyTorch tensor back to a standard NumPy array for drawing graphs
    eeg_data = eeg_tensor.numpy()

    print("[INFO] Generating Time-Domain Graph...")
    
    # 3. GRAPH 1: Time-Domain (Voltage over 1 Second)
    # We will only plot the first 3 channels (AF3, F7, F3) so the graph isn't too messy
    channel_names = ['AF3 (Frontal)', 'F7 (Frontal)', 'F3 (Frontal)']
    time_axis = np.linspace(0, 1.0, 128)  # 128 points spread evenly across 1 second

    plt.figure(figsize=(10, 5))
    for i in range(3):
        # We add (i * 50) as a vertical offset so the 3 lines don't crash into each other
        plt.plot(time_axis, eeg_data[i, :] + (i * 50), label=channel_names[i])
    
    plt.title(f"Raw EEG Time Series (Class Label: {label.item()})")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Amplitude (Microvolts)")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show() # This pauses the script and opens the first window

    print("[INFO] Generating Frequency-Domain Graph (PSD)...")

    # 4. GRAPH 2: Frequency-Domain (Power Spectral Density)
    # This uses Welch's method to find dominant frequencies and check for 50Hz wall noise
    plt.figure(figsize=(10, 5))
    for i in range(3):
        # Calculate frequencies and their power using SciPy
        frequencies, psd = signal.welch(eeg_data[i, :], fs=128, nperseg=128)
        plt.semilogy(frequencies, psd, label=channel_names[i])

    plt.title("Power Spectral Density (Checking for Noise)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power (Log Scale)")
    plt.xlim(0, 60) # We only care about 0 to 60 Hz for brainwaves
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show() # This pauses the script and opens the second window

    print("=" * 60)
    print("✅ DAY 2 VISUALIZATION COMPLETE.")
    print("=" * 60)

if __name__ == "__main__":
    run_day2_visualization()