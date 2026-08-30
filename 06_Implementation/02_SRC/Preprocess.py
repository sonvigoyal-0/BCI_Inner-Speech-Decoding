import numpy as np
from scipy.signal import butter, filtfilt

def apply_bandpass_filter(data, lowcut=1.0, highcut=40.0, fs=128, order=4):
    """
    Ek Bandpass filter jo sirf 1 Hz se 40 Hz ke brainwaves ko pass hone dega.
    Data expected shape: (Channels, Time) -> (14, 128)
    """
    # 1. Nyquist Theorem: Hum sampling rate ka aadha max map sakte hain
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    
    # 2. Filter ka design banana (Butterworth filter)
    b, a = butter(order, [low, high], btype='band')
    
    # 3. Data par filter apply karna (axis=1 matlab time par filter lagao)
    filtered_data = filtfilt(b, a, data, axis=1)
    
    # Data ko wapas float32 mein convert karna AI ke liye
    return filtered_data.astype(np.float32)

if __name__ == "__main__":
    # Test karne ke liye ek dummy (fake) data banate hain
    print("[INFO] Testing Bandpass Filter...")
    dummy_data = np.random.rand(14, 128) # 14 channels, 128 samples
    clean_data = apply_bandpass_filter(dummy_data)
    
    print(f"Original Shape: {dummy_data.shape}")
    print(f"Cleaned Shape : {clean_data.shape}")
    print("✅ Filter is working properly without changing the matrix shape.")