# A Low-Latency Neural Inference Framework for Real-Time Handwriting Recognition from EEG Signals on an Edge Device

---

## Paper Information :-

| Field | Details |
|-------|---------|
| **Title** | A Low-Latency Neural Inference Framework for Real-Time Handwriting Recognition from EEG Signals on an Edge Device |
| **Authors** | Ovishake Sen, Raghav Soni, Darpan Virmani, Akshar Parekh, Patrick Lehman, Sarthak Jena, Adithi Katikhaneni, Adam Khalifa, Baibhab Chatterjee |
| **Year** | 2025 |
| **Journal** | Scientific Reports (Nature Portfolio) |
| **Primary Focus** | Real-Time Imagined Handwriting Recognition from EEG |

---

## Summary :-

This paper presents the first real-time, low-latency framework for decoding imagined handwriting from non-invasive EEG signals directly on an edge device. The authors combine efficient EEG preprocessing, handcrafted feature extraction, Pearson correlation-based feature selection, and a lightweight deep learning architecture (EEdGeNet) to achieve high classification accuracy while minimizing inference latency. The trained model is deployed on an NVIDIA Jetson TX2, demonstrating that portable EEG-based neural decoding is feasible for practical Brain-Computer Interface applications.

---

## Research Objective :-

The primary objective of this research is to develop a practical EEG decoding framework capable of:

- Performing real-time imagined handwriting recognition.
- Reducing inference latency.
- Deploying directly on low-power edge hardware.
- Maintaining high classification accuracy without invasive neural recording.

---

## Problem Statement :-

Existing handwriting decoding systems mainly rely on invasive techniques such as:

- ECoG
- Utah Arrays
- Intracortical Electrodes

Although these systems achieve excellent accuracy, they require brain surgery and are unsuitable for widespread use.

On the other hand, EEG-based systems are safe and portable but suffer from:

- Low Signal-to-Noise Ratio (SNR)
- Poor spatial resolution
- High computational complexity
- Slow inference speed
- Limited real-time deployment

This work attempts to overcome these limitations by combining efficient signal processing with a lightweight neural architecture optimized for edge deployment.

---

# Dataset Overview :-

## Participants

- 15 healthy participants

## EEG Hardware

- 32-channel EEG headcap

## Recording Paradigm

Participants imagined writing characters without performing any physical movement.

The recorded EEG signals represent motor intentions associated with handwriting.

---


# EEG Preprocessing :-

The preprocessing pipeline consists of several stages designed to improve signal quality while minimizing computational cost.

## 1. Band-pass Filtering

Purpose:

- Remove low-frequency drift
- Remove high-frequency noise
- Preserve useful EEG activity

---

## 2. Artifact Subspace Reconstruction (ASR)

ASR removes artifacts produced by:

- Eye blinks
- Muscle activity
- Head movement
- Electrical interference

Unlike ICA, ASR is computationally efficient and better suited for real-time applications.

---

## 3. Signal Segmentation

Continuous EEG recordings are divided into individual character windows.

Each segment corresponds to one imagined handwriting trial.

---

# Feature Extraction

Instead of training directly on raw EEG signals, the authors extract handcrafted features.

A total of **85 features** are extracted from every EEG segment.

These features belong to three categories:

## Time-Domain Features

Examples:

- Root Mean Square (RMS)
- Variance
- Hjorth Mobility
- Hjorth Complexity

These describe signal amplitude and temporal behavior.

---

## Frequency-Domain Features

Examples:

- Delta Power
- Mean Dominant Frequency
- Spectral Power

These capture oscillatory brain activity.

---

## Graphical Features

Graphical descriptors are extracted from geometric representations of EEG signals.

Examples:

- Ellipse Area
- Distance Metrics
- Phase-space descriptors

These provide complementary spatial information.

---

# Why Handcrafted Features?

Instead of feeding raw EEG into a very deep neural network, the authors first extract informative features because:

- Noise is reduced.
- Model complexity decreases.
- Inference becomes faster.
- Edge deployment becomes feasible.
- Energy consumption is reduced.

This design choice is central to achieving low-latency decoding. 

---

# Feature Selection

Not all 85 features contribute equally.

The authors apply **Pearson Correlation Coefficient** to rank feature importance and remove redundant features.

Benefits:

- Faster inference
- Lower memory usage
- Reduced computational cost
- Nearly unchanged accuracy

This step is crucial for enabling deployment on resource-constrained devices. 

---

## Motivation :-

The authors aim to bridge the gap between:
- High-performance invasive BCIs
- Practical non-invasive BCIs
Their goal is to build a portable neural decoding system capable of translating imagined handwriting into text with minimal latency.

---
