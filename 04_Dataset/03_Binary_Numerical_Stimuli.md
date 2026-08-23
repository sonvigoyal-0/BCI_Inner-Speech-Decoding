# Dataset 3: EEG Imagined Speech Dataset for BCI Applications with Binary and Numerical Stimuli



## Overview

This dataset is developed for imagined speech Brain-Computer Interface (BCI) research. It contains EEG recordings collected while participants silently imagined binary and numerical words without any actual speech or muscle movement.

The dataset focuses on simple command-based imagined speech, making it appropriate for studying real-time BCI communication systems and lightweight command decoding.

---

# Dataset Summary

| Parameter | Details |
|-----------|---------|
| Number of Participants | 30 Healthy Subjects |
| Average Age | Approximately 20.5 Years |
| Gender Distribution | 22 Male, 8 Female |
| EEG Headset | Unicorn Hybrid Black |
| Number of Channels | 8 |
| Sampling Rate | 250 Hz |
| Signal Resolution | 24-bit |
| Language | Spanish |
| License | CC BY-NC-SA 4.0 |

---

# Hardware Configuration

The EEG recordings were recorded using the **Unicorn Hybrid Black** wireless headset, a portable and non-invasive EEG acquisition system commonly used for BCI research.

The headset records signals from **8 active EEG channels** placed over regions linked with motor planning and cognitive processing.

### Electrode Locations

- Fz
- C3
- Cz
- C4
- Pz
- PO7
- Oz
- PO8

These electrode locations provide suitable coverage of the central, sensorimotor, parietal, and occipital brain regions that are commonly investigated in imagined speech studies.

---

# Experimental Design

The experiment is divided into two imagined speech paradigms.

1. **Binary Paradigm** :-

Participants silently imagine binary responses such as:

- Yes
- No


2. **Numerical Paradigm** :-

Participants silently imagine numerical commands.

The union of binary and numerical stimuli creates a total of **five target classes**, allowing the dataset to be used for multi-class EEG classification.

---

# Data Organization

The dataset is well organized and easy to locate.

The recordings are structred according to:

- Individual participants
- Experimental paradigm
- Target command

Each recording contains synchronized multichannel EEG time-series data representing the participant's imagined speech activity.

---

# Why We Selected This Dataset :-

This dataset aligns well with the objectives of our research project for various reasons.

1. **Lightweight EEG Acquisition** - The dataset uses only **8 EEG channels**, making it closer to practical wearable BCI systems than high-density laboratory setups.

This allows us to examine whether lightweight decoding models can still attain reliable performance under realistic hardware constraints.


2. **Cross-Subject Examination** - It includes **30 participants** which provides enough diversity for evaluating subject-independent models.

It also supports **Leave-One-Subject-Out (LOSO)** testing, which is an important evaluation strategy for testing model generalization across unseen users.


3. **Practical Command-Based Design** -  Instead of focusing on complex vocabulary, the dataset uses simple binary and numerical commands.

Such commands are directly applicable to real-world BCI interfaces, including:

- Menu navigation
- Communication systems
- Smart device control
- Emergency response interfaces


4. **Suitable for Edge AI Research** - The mixture of:

- 8-channel EEG
- 250 Hz sampling rate
- Simple command classes

makes this dataset perfect for developing computationally efficient models intended for real-time edge deployment.

---


# Limitations :-

Although the dataset is valuable, multiple practical limitations should be looked :-

1. **Limited Vocabulary** - The dataset contains only binary and numerical imagined speech commands.

It cannot be used to evaluate large-vocabulary imagined speech decoding.


2. **Language Dependency** - The recordings were collected using Spanish stimuli.

Models trained on this dataset may needs further verifications before being applied to other languages.


3. **Low Spatial Resolution** - Only eight EEG channels are available.

Whereas it supports lightweight hardware, and may also finite the amount of spatial information available for decoding more complex neural patterns.


4. **Controlled Recording Environment** - The recordings were gathered under controlled experimental conditions, due to which performance in real-world environments with motion artifacts and environmental noise may differ.

---

# Relevance to Our Project

This dataset is well aligned with our research objectives.

It supports the examination of:

- Low-latency EEG decoding
- Lightweight BCI architectures
- Cross-subject generalization
- Edge AI deployment
- Command-based imagined speech interfaces

Although the vocabulary is narrow, it provides an outstanding initial point for validating robust and computationally efficient imagined speech decoding methods before extending the approach to larger vocabularies.

---

# Reference

**Dataset Title**

*An EEG Imagined Speech Dataset for BCI Applications with Binary and Numerical Stimuli*

**Source**

Figshare

**License**

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)