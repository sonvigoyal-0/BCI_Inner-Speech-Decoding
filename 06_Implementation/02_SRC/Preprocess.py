import numpy as np
from scipy.signal import butter, filtfilt

def apply_bandpass_filter(data, lowcut=1.0, highcut=40.0, fs=128, order=4):
    """Applies a 1-40Hz Bandpass filter."""
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    filtered_data = filtfilt(b, a, data, axis=1)
    return filtered_data

def apply_z_score_normalization(data):
    """
    Standardizes the data so mean=0 and variance=1 per channel.
    Input shape: (Channels, Time)
    """
    mean =  np.mean(data, axis=1, keepdims=True)
    std = np.std(data, axis=1, keepdims=True)
    
    # Prevent division by zero if a channel is flat
    std[std == 0] = 1e-6
    
    normalized_data = (data - mean) / std
    return normalized_data

def preprocess_pipeline(data):
    """Master function to run all preprocessing steps."""
    # Step 1: Remove noise frequencies
    filtered = apply_bandpass_filter(data)
    
    # Step 2: Scale numbers for AI
    normalized = apply_z_score_normalization(filtered)
    
    return normalized.astype(np.float32)

if __name__ == "__main__":
    print("[INFO] Testing Full Preprocessing Pipeline...")
    dummy_data = np.random.rand(14, 128) * 100 
    clean_data = preprocess_pipeline(dummy_data)
    
    print(f"New Mean (Should be ~0.0): {np.mean(clean_data[0]):.2f}")
    print(f"New Std Dev (Should be ~1.0): {np.std(clean_data[0]):.2f}")
    print("✅ Pipeline ready.")