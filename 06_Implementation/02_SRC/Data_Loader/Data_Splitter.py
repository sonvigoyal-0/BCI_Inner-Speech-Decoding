import os
import sys
import torch
from torch.utils.data import Subset, DataLoader
from sklearn.model_selection import train_test_split

# Import our Day 1/3 Dataset
from EEGIS_dataset import EEGISDataset

def get_stratified_dataloaders(dataset_dir, batch_size=32):
    """
    Splits the EEGIS dataset into 80% Train, 10% Validation, and 10% Test.
    Uses stratification to ensure all 9 classes are equally represented in each split.
    """
    # 1. Load the full dataset (This applies our filters from Day 3)
    full_dataset = EEGISDataset(root_dir=dataset_dir)
    
    # 2. Extract just the labels so we can stratify (balance) the split
    all_labels = [label for _, label in full_dataset.samples]
    indices = list(range(len(full_dataset)))
    
    # 3. First Split: Separate out 20% for Val + Test (Leaves 80% for Train)
    train_idx, temp_idx, _, temp_labels = train_test_split(
        indices, all_labels, test_size=0.20, stratify=all_labels, random_state=42
    )
    
    # 4. Second Split: Cut that 20% in half to get 10% Val and 10% Test
    val_idx, test_idx = train_test_split(
        temp_idx, test_size=0.50, stratify=temp_labels, random_state=42
    )
    
    # 5. Create PyTorch Subsets locking the data into these splits
    train_dataset = Subset(full_dataset, train_idx)
    val_dataset = Subset(full_dataset, val_idx)
    test_dataset = Subset(full_dataset, test_idx)
    
    # 6. Wrap them in DataLoaders (Train gets shuffled, Val/Test do not)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader, test_loader, len(full_dataset)

if __name__ == "__main__":
    print("=" * 60)
    print(" LEAKAGE-FREE DATA SPLITTING")
    print("=" * 60)
    

    dataset_dir = os.path.join("06_Implementation", "01_Data", "Raw", "EEGIS", "raw")
    
    try:
        train_loader, val_loader, test_loader, total_size = get_stratified_dataloaders(dataset_dir)
        
        print(f"[INFO] Total Trials   : {total_size}")
        print(f"[INFO] Training Set   : {len(train_loader.dataset)} trials (80%)")
        print(f"[INFO] Validation Set : {len(val_loader.dataset)} trials (10%)")
        print(f"[INFO] Test Set       : {len(test_loader.dataset)} trials (10%)")
        print("✅ Data splitting complete. Leakage prevented.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")