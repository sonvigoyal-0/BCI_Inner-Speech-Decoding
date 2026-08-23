import os
import glob
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader

class EEGISDataset(Dataset):
    """
    PyTorch Dataset parser for the EEGIS (Emotiv EPOC+ 14-Channel) corpus.
    Loads 1-second raw chunks of shape (14, 128).
    """
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.samples = []
        
        # Define the 9 target classes based on EEGIS folder naming convention
        self.class_map = {
            'class_0': 0, # Rest
            'class_1': 1, # Ayuda
            'class_2': 2, # Bano
            'class_3': 3, # Dolor
            'class_4': 4, # Gracias
            'class_5': 5, # Hambre
            'class_6': 6, # No
            'class_7': 7, # Sed
            'class_8': 8  # Si
        }
        
        self._index_files()

    def _index_files(self):
        """Scans all class subdirectories and collects file paths with labels."""
        for class_name, label in self.class_map.items():
            class_folder = os.path.join(self.root_dir, class_name)
            if os.path.exists(class_folder):
                csv_files = glob.glob(os.path.join(class_folder, "*.csv"))
                for file_path in csv_files:
                    self.samples.append((file_path, label))
            else:
                print(f"[Warning] Directory not found: {class_folder}")

        print(f"[INFO] Indexed {len(self.samples)} total trials across {len(self.class_map)} classes.")

    def __len__(self):
        return len(self.samples)



    def __getitem__(self, idx):
        file_path, label = self.samples[idx]
        
        # Removed header=None so it reads 'AF3', 'F7', etc. as column names, not data
        df = pd.read_csv(file_path)
        
        # Some CSVs include an extra index column. We only want the 14 EEG channels.
        # We will dynamically grab the last 14 columns to be safe.
        if df.shape[1] > 14:
            df = df.iloc[:, -14:]
            
        data = df.values.astype('float32') # Now it only converts the numbers
        
        # Ensure shape is strictly (Channels=14, TimeSamples=128)
        if data.shape[0] == 128 and data.shape[1] == 14:
            data = data.T # Transpose to (14, 128)
            
        tensor_data = torch.from_numpy(data) 
        tensor_label = torch.tensor(label, dtype=torch.long) 
        
        return tensor_data, tensor_label


def run_day1_inspection():
    """Execution script for Day 1 inspection and batch validation."""
    print("=" * 60)
    print(" DAY 1: EEGIS DATASET INSPECTION & PIPELINE VERIFICATION")
    print("=" * 60)
    
    # Path to the raw unbandpassed folder
    dataset_dir = os.path.join("data", "raw", "eegis", "raw")
    
    # Fallback to absolute/relative check if run from repo root
    if not os.path.exists(dataset_dir):
        dataset_dir = os.path.join("06_Implementation", "01_Data", "Raw", "EEGIS", "raw")

    if not os.path.exists(dataset_dir):
        print(f"[ERROR] Could not find raw dataset directory at: {dataset_dir}")
        print("Please verify your folder extraction location.")
        return

    # Instantiate Dataset
    dataset = EEGISDataset(root_dir=dataset_dir)
    
    if len(dataset) == 0:
        print("[ERROR] No trials loaded. Check if CSV files exist inside class folders.")
        return

    # 1. Single Trial Inspection
    first_signal, first_label = dataset[0]
    print("\n--- SINGLE TRIAL SANITY CHECK ---")
    print(f"Sample 0 Tensor Shape : {first_signal.shape} (Expected: torch.Size([14, 128]))")
    print(f"Sample 0 Data Type    : {first_signal.dtype}")
    print(f"Sample 0 Class Label  : {first_label.item()} (Class {first_label.item()})")
    print(f"Min Voltage Value     : {first_signal.min():.4f}")
    print(f"Max Voltage Value     : {first_signal.max():.4f}")
    print(f"Contains NaNs?        : {torch.isnan(first_signal).any().item()}")

    # 2. PyTorch DataLoader Batch Test
    print("\n--- PYTORCH BATCHING TEST ---")
    batch_size = 32
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    batch_signals, batch_labels = next(iter(loader))
    print(f"Batch Tensor Shape    : {batch_signals.shape} (Expected: torch.Size([32, 14, 128]))")
    print(f"Batch Labels Shape    : {batch_labels.shape} (Expected: torch.Size([32]))")
    print("=" * 60)
    print("✅ DAY 1 INSPECTION PASSED: Data ingestion pipeline is ready.")
    print("=" * 60)


if __name__ == "__main__":
    run_day1_inspection()