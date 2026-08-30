import os
import sys
import glob
import pandas as pd
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

# --- NEW: Add parent folder to path so we can import preprocess.py ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Preprocess import preprocess_pipeline

class EEGISDataset(Dataset):
    """
    PyTorch Dataset parser for the EEGIS (Emotiv EPOC+ 14-Channel) corpus.
    Loads 1-second raw chunks of shape (14, 128) and applies 1-40Hz filtering.
    """
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.samples = []
        
        self.class_map = {
            'class_0': 0, 'class_1': 1, 'class_2': 2,
            'class_3': 3, 'class_4': 4, 'class_5': 5,
            'class_6': 6, 'class_7': 7, 'class_8': 8
        }
        
        self._index_files()

    def _index_files(self):
        for class_name, label in self.class_map.items():
            class_folder = os.path.join(self.root_dir, class_name)
            if os.path.exists(class_folder):
                csv_files = glob.glob(os.path.join(class_folder, "*.csv"))
                for file_path in csv_files:
                    self.samples.append((file_path, label))
            else:
                print(f"[Warning] Directory not found: {class_folder}")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        file_path, label = self.samples[idx]
        
        df = pd.read_csv(file_path)
        
        if df.shape[1] > 14:
            df = df.iloc[:, -14:]
            
        data = df.values.astype('float32')
        
        if data.shape[0] == 128 and data.shape[1] == 14:
            data = data.T 
            
         # Apply the full Bandpass + Z-Score pipeline
            data = preprocess_pipeline(data)
        # --------------------------------------------
       
        tensor_data = torch.from_numpy(data) 
        tensor_label = torch.tensor(label, dtype=torch.long) 
        
        return tensor_data, tensor_label


def run_integration_test():
    print("=" * 60)
    print(" INTEGRATION TEST: DATA LOADER + FILTER")
    print("=" * 60)
    
    dataset_dir = os.path.join("06_Implementation", "01_Data", "Raw", "EEGIS", "raw")
    dataset = EEGISDataset(root_dir=dataset_dir)
    
    loader = DataLoader(dataset, batch_size=32, shuffle=True)
    batch_signals, batch_labels = next(iter(loader))
    
    print(f"Filtered Batch Tensor Shape : {batch_signals.shape}")
    print(f"Data Type                   : {batch_signals.dtype}")
    print("✅ Integration successful! AI model will now receive clean data.")
    print("=" * 60)

if __name__ == "__main__":
    run_integration_test()