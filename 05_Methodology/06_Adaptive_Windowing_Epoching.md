# Adaptive Windowing with Lightweight CNN

## What is it?
This methodology is an "event-driven" approach designed specifically for extremely low-latency, low-power, and edge-deployable thought-to-text systems. Instead of running a heavy artificial intelligence model continuously on a stream of brainwaves, the system uses a change-detection formula to figure out exactly when a thought begins, and only runs the AI on that specific snippet of data.

## How does it actually work? (The Step-by-Step Pipeline)
1. **Continuous Monitoring:** The system continuously monitors the incoming multi-channel EEG signals using a mathematical technique called CUSUM (Cumulative Summation) change detection.
2. **The Trigger:** When the CUSUM detects a significant change in the signal's variance—indicating the onset of inner speech or a thought—it acts as a trigger.
3. **Adaptive Windowing:** Upon triggering, the system opens an "adaptive window" to capture *only* the relevant, active segment of the brainwave.
4. **Lightweight Decoding:** This captured segment is then passed into a lightweight Convolutional Neural Network (CNN), such as EEGNet, to decode the thought into text. 

## Why is it Useful? (Advantages)
* **Lightning Fast (Low Latency):** It completely eliminates the delay caused by waiting for fixed time boundaries to finish recording before processing the data.
* **Extreme Power Efficiency:** The AI model only runs inference during active thought events[cite: 6]. This drastically reduces the computational workload, making it ideal for battery-operated wearables and embedded devices like a Raspberry Pi or NVIDIA Jetson.
* **Ignores "Idle" Noise:** By waiting for a specific trigger, the system prevents normal background brain activity or idle state noise from generating false text outputs.
* **Captures the Whole Thought:** It captures the full, variable-length duration of the thought without unnecessarily chopping it off (truncation) or filling empty space with fake data (padding).

## Limitations
* **The Threshold Problem:** Choosing the absolute perfect CUSUM threshold is highly important for the system to work.
* **False Triggers:** If the system triggers incorrectly, it can negatively affect the overall accuracy of the text decoding.


# Phase-Locked Adaptive Epoching with Dual-Branch Deep Learning

## What is it?
This methodology is a highly robust, neurophysiologically grounded approach to capturing thoughts. Instead of looking at the raw electrical volume (amplitude) of brainwaves to detect a thought, this method looks at the "phase"—the underlying rhythm and synchronization of the brain's oscillations, like theta or alpha rhythms. 

## How does it actually work? (The Step-by-Step Pipeline)
1. **Phase Tracking:** The system tracks the Instantaneous Phase-Locking Value (iPLV) of the brainwaves. Inner speech activates functional networks in the brain that synchronize their phases when communicating.
2. **The Smart Trigger:** When the system detects that phase synchronization (iPLV) has increased, it triggers an adaptive window (or "epoch") to open. 
3. **Closing the Window:** The window closes cleanly as soon as the synchronization drops, ensuring only the true duration of the cognitive thought is captured.
4. **Dual-Branch Decoding:** These clean brainwave segments are passed to a "dual-branch" deep learning network[cite: 6]. 
    *   One branch analyzes the time-domain (temporal dynamics).
    *   The second branch analyzes the frequency-domain (spectral patterns).
5. **Fusion:** The two branches are fused together to make a highly accurate final prediction.

## Why is it Useful? (Advantages)
* **Highly Resistant to Physical Noise:** Raw voltage amplitude fluctuates wildly and is extremely sensitive to physical noise like muscle artifacts, eye blinks, and scalp sweat, which causes high false trigger rates. Phase synchronization reflects true brain communication and is highly robust to these non-neural physical noises.
* **Richer Data Representation:** Inner speech carries important information in both time and frequency domains simultaneously. The dual-branch design perfectly captures *when* patterns occur and *what* frequencies they involve.
* **Stable Across Users and Days:** Because rhythmic phase relationships are much more stable neural markers than raw amplitude, this method is far less likely to be thrown off by signal variability across different recording sessions or entirely different users. 

## Limitations
* **High Complexity:** This method requires much more complex signal processing compared to standard amplitude monitoring.
* **Heavy Computing:** Analyzing phase and running a dual-branch network results in higher computational requirements.
* **Strict Estimation:** The system requires very careful and precise phase estimation to function correctly.