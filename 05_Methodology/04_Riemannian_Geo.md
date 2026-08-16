# Riemannian Geometry-Based Classification for BCI

## What is it?
Instead of using a heavy deep neural network to "learn" patterns from scratch, this method treats each window of brain signals as a geometric shape in space. Specifically, it analyzes how the electrical signals from different electrodes relate to one another (their covariance) and treats that relationship as a point on a curved mathematical surface called a "Riemannian manifold". 

## How does it actually work? (The Step-by-Step Pipeline)
1. **Signal Acquisition:** Multi-channel EEG data is recorded from the scalp.
2. **Preprocessing:** Signals are filtered using a bandpass filter to remove gross noise, eye blinks, and muscle artifacts.
3. **Feature Extraction (The Covariance Matrix):** For a short time window of EEG data, the system computes a covariance matrix. This acts as a mathematical summary matrix that defines how every single electrode's signal relates to every other electrode. This matrix is Symmetric Positive-Definite (SPD).
4. **Mapping to the Manifold:** Because SPD matrices do not fit neatly onto a flat grid, they are mapped onto a curved Riemannian manifold (visualized as a curved bowl surface). Measuring distances on this curved space is far more stable against daily signal changes (like electrode impedance shifts) than a flat Euclidean space.
5. **Classification:** To classify a thought, the system simply measures the geometric distance between the new brain-signal "shape" and the average shape stored for each known word or command. Whichever average shape is closest wins the classification.

## Why is it Useful?
* **Lightning Fast:** Because it skips the heavy, time-consuming training process of deep learning neural networks, math-based matrix comparison is much faster, perfectly supporting real-time, low-latency BCI goals.
* **Naturally Robust:** The Riemannian metric naturally handles minor day-to-day signal drift and electrode position shifts.
* **Data Efficient:** It requires far less training data than deep neural networks and remains completely interpretable.

## Limitations
* **Limited Complexity:** Because it only focuses on broad signal relationships rather than fine temporal details, it struggles to accurately decode complex tasks like full, open-ended imagined speech.
* **Vocabulary Cap:** It works very well for small command menus (a few discrete classes), but has not been proven effective for large-vocabulary text decoding