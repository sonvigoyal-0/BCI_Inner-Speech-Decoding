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



# Spiking Neural Networks (SNNs) for Event-Driven Decoding

## What is an SNN?
Spiking Neural Networks (SNNs) are bio-inspired artificial intelligence models designed to function like biological brains. Instead of processing continuous streams of numbers at every single millisecond (like standard AI), SNNs process information using discrete "spikes" over time, computing *only* when an event happens.

## How does it actually work? (The Step-by-Step Pipeline)
1. **Signal Acquisition & Preprocessing:** Raw EEG signals are collected and cleaned using standard bandpass filters.
2. **Event-Based Encoding (Thresholding):** Continuous brainwaves are converted into sparse spike trains[cite: 5]. A spike (value of 1) is generated *only* when the EEG signal crosses a predefined positive or negative voltage threshold. Small background fluctuations are ignored, making it naturally noise-robust.
3. **SNN Processing (Leaky Integrate-and-Fire Neurons):** These spike trains are fed into artificial spiking neurons. Every incoming spike increases the neuron's internal electrical charge (membrane potential). If no spikes arrive, the potential slowly leaks away over time.
4. **Firing & Propagation:** When a neuron's accumulated potential hits its threshold, it fires an output spike and resets, mimicking real biological brain cells. 
5. **Classification:** SNNs analyze spatiotemporal patterns—meaning they care precisely *when* the spikes arrive, not just how many occur. Output neurons compete, and the category with the highest spike count during the decision window wins.

## Why is it Useful?
* **Extreme Energy Efficiency:** Standard AI models consume heavy computing power because they process data at every single time step. SNNs are event-driven, meaning they only compute when spikes occur. This drastically reduces power consumption, which is crucial for wearable, always-on BCI systems.
* **True Low-Latency:** Decisions can be made as soon as enough spike events are observed, without waiting for fixed-length sliding windows.

## Limitations
* **Hardware Dependence:** To unlock the real speed and power-saving advantages of an SNN, you must run it on specialized "neuromorphic hardware" (computer chips built to mimic biological brain structures, like the IBM North Pole or True North chips). If simulated on a standard computer or GPU, most of those efficiency gains disappear.
* **Immature Technology:** SNNs are newer and much harder to train than traditional neural networks, and they generally trail behind standard deep learning models in raw classification accuracy.