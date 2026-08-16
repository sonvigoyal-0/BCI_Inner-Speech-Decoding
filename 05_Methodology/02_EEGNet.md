# EEGNet: The Brainwave Feature Extractor

## What exactly is EEGNet?
EEGNet is a specialized **Convolutional Neural Network (CNN)**. 

Usually, CNNs are used for image recognition (like teaching an AI to recognize a cat in a photo by looking at pixels). However, instead of looking at a 2D grid of pixels, EEGNet looks at a 2D grid of **brainwave data** (Time vs. Electrodes). 

It is a mathematical filter. You feed it a 150-millisecond snippet of raw, noisy electrical voltage from the brain, and it mathematically squashes, filters, and transforms that noise into a neat list of numbers (a "feature vector") that represents the core thought or intent.

## How does it actually work? (Architecture)
Standard AI models look at all the data at once, which requires massive computing power. EEGNet is clever because it breaks the decoding process into three distinct, highly efficient layers:

*   **Layer 1: Temporal Convolution (The Frequency Filter)**
    Instead of looking at the whole brain, this layer only looks at **time**. It scans the horizontal electrical waves and acts like an audio equalizer. It filters out the "static" and isolates specific brainwave frequencies (like Alpha or Beta waves) that are active during imagined speech.
*   **Layer 2: Depthwise Spatial Convolution (The Location Filter)**
    Now that the AI has isolated the right frequencies, it looks vertically across the **electrodes**. It learns *where* on the scalp these frequencies are the strongest. It essentially draws a map connecting the active brain regions.
*   **Layer 3: Separable Convolution (The Compressor)**
    Finally, the network takes the frequency data (Layer 1) and the location map (Layer 2) and safely blends them together. It compresses this massive amount of data into a tiny, dense summary (the feature vector) without losing the important neural information.

## Why use it over other models?
Because it separates the "Time" filter from the "Space" filter, EEGNet only needs about 1,000 to 3,000 parameters to do its job. A standard Transformer model would need millions. This means EEGNet can run in under 5 milliseconds on a tiny edge device (like a Jetson TX2) without overheating.

## Limitations
*   **Artifact Blindness:** It only extracts what you feed it. If you feed it a jaw clench or an eye blink, it will perfectly extract the features of a jaw clench, ruining your text output.
*   **Requires Tuning:** While it is a great default architecture, you must manually adjust its mathematical window sizes (kernels) to match the exact length of the phonemes or words you are trying to detect.