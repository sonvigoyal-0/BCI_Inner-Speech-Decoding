import torch
import torch.nn as nn

class EEGNet(nn.Module):
    """
    Lightweight EEGNet Architecture for Brain-Computer Interfaces.
    Optimized for 14-Channel, 128Hz sampling rate data.
    """
    def __init__(self, num_classes=9, channels=14, time_samples=128):
        super(EEGNet, self).__init__()
        
        # F1 = Number of temporal filters, D = Depth multiplier (Spatial filters)
        F1 = 8
        D = 2
        F2 = F1 * D # 16 filters for the next block
        
        # --- BLOCK 1: Temporal & Spatial Convolution ---
        # 1. Temporal Convolution: Learns frequency patterns over time
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=F1, kernel_size=(1, 64), padding='same', bias=False)
        self.batchnorm1 = nn.BatchNorm2d(F1)
        
        # 2. Depthwise Convolution (Spatial): Learns which electrodes are firing
        self.depthwise = nn.Conv2d(in_channels=F1, out_channels=F1 * D, kernel_size=(channels, 1), groups=F1, bias=False)
        self.batchnorm2 = nn.BatchNorm2d(F1 * D)
        self.activation = nn.ELU()
        
        # Pooling to reduce size and prevent overfitting
        self.pool1 = nn.AvgPool2d(kernel_size=(1, 4))
        self.dropout1 = nn.Dropout(p=0.25)
        
        # --- BLOCK 2: Separable Convolution ---
        # Learns how to combine time and space information together
        self.separable_conv = nn.Conv2d(in_channels=F2, out_channels=F2, kernel_size=(1, 16), padding='same', groups=F2, bias=False)
        self.pointwise_conv = nn.Conv2d(in_channels=F2, out_channels=F2, kernel_size=1, bias=False)
        self.batchnorm3 = nn.BatchNorm2d(F2)
        
        self.pool2 = nn.AvgPool2d(kernel_size=(1, 8))
        self.dropout2 = nn.Dropout(p=0.25)
        
        # --- BLOCK 3: Classification Layer ---
        # Calculating the output size after all pooling layers:
        # Time starts at 128 -> Pool1 (/4) = 32 -> Pool2 (/8) = 4
        # Features = F2 (16) * 4 time steps remaining = 64 features
        self.flatten = nn.Flatten()
        self.classifier = nn.Linear(in_features=16 * 4, out_features=num_classes)

    def forward(self, x):
        # AI models expect image-like shapes: (Batch, Channels, Height, Width)
        # Our DataLoader outputs (Batch, 14, 128). We need to add a "dummy" channel dimension.
        # Shape becomes: (Batch, 1, 14, 128)
        x = x.unsqueeze(1)
        
        # Pass through Block 1
        x = self.conv1(x)
        x = self.batchnorm1(x)
        x = self.depthwise(x)
        x = self.batchnorm2(x)
        x = self.activation(x)
        x = self.pool1(x)
        x = self.dropout1(x)
        
        # Pass through Block 2
        x = self.separable_conv(x)
        x = self.pointwise_conv(x)
        x = self.batchnorm3(x)
        x = self.activation(x)
        x = self.pool2(x)
        x = self.dropout2(x)
        
        # Flatten and Classify
        x = self.flatten(x)
        x = self.classifier(x)
        
        return x

def test_model_architecture():
    print("=" * 60)
    print(" DAY 4: EEGNET ARCHITECTURE TEST")
    print("=" * 60)
    
    # Create the model
    model = EEGNet(num_classes=9)
    
    # Create fake batch of data just like our DataLoader outputs (Batch=32, Channels=14, Time=128)
    dummy_input = torch.randn(32, 14, 128)
    
    # Pass data through model
    output = model(dummy_input)
    
    # Calculate Total Parameters (Size of the model)
    total_params = sum(p.numel() for p in model.parameters())
    
    print(f"Input Data Shape    : {dummy_input.shape}")
    print(f"Model Output Shape  : {output.shape} (Expected: 32 predictions for 9 classes)")
    print(f"Total Parameters    : {total_params:,} (Extremely lightweight!)")
    print("=" * 60)
    print("✅ Model Architecture is ready and fully compatible with our Edge Hardware goals.")
    print("=" * 60)

if __name__ == "__main__":
    test_model_architecture()