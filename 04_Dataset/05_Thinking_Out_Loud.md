# Dataset 5: Thinking Out Loud – EEG-Based Inner Speech Recognition Dataset

---

# Overview

This dataset was developed to support research on EEG-based inner speech recognition. It contains brain activity recorded while participants either imagined speaking a word, pronounced the word aloud, or performed a visual imagination task.

In contrast to many imagined speech datasets, this dataset also includes facial EMG recordings to verify that participants were not unintentionally moving their speech muscles during the inner speech trials. This makes it particularly valuable for studying genuine neural activity associated with silent speech.

The dataset is publicly available through OpenNeuro and follows the Brain Imaging Data Structure (BIDS) standard, making it straightforward to use with common EEG analysis tools.

---

# Dataset Summary

| Parameter | Details |
|-----------|---------|
| Number of Participants | 10 Healthy Subjects |
| Gender Distribution | 6 Male, 4 Female |
| EEG System | BioSemi ActiveTwo |
| EEG Channels | 64 |
| Additional Sensors | 4 EOG, 2 EMG, Mastoid References |
| Sampling Rate | 1024 Hz |
| Recording Sessions | Up to 5 Sessions Across 3 Days |
| Vocabulary Size | 4 Directional Words |
| Data Format | BIDS (.bdf) |
| Dataset Source | OpenNeuro (ds003626) |

---


# Experimental Design

Each participant completed three different experimental conditions using the same visual cues.

1. **Inner Speech** - Participants silently imagined pronouncing the displayed word without producing any sound or facial movement.


2. **Pronounced Speech** - Participants spoke the displayed word aloud.

This condition provides a useful reference for understanding how overt speech differs from inner speech.


3. **Visualized Condition** - Participants imagined the movement indicated by the visual cue rather than imagining the spoken word.

This serves as an additional comparison task during analysis.

---

# Hardware Configuration

The recordings were collected using the **BioSemi ActiveTwo** EEG acquisition system inside an electrically shielded recording room.

The setup includes:

- 64 active EEG electrodes
- 4 Electrooculography (EOG) channels
- 2 Electromyography (EMG) channels
- Mastoid reference electrodes

Apart EOG and EMG channels help identify eye movements and facial muscle activity, improving the quality of the EEG recordings during preprocessing.

---


# Vocabulary

The experiment uses four directional commands.

- Arriba (Up)
- Abajo (Down)
- Derecha (Right)
- Izquierda (Left)

The limited vocabulary keeps the classification task focused while allowing researchers to study the neural representation of imagined words.

---

# Trial Structure

Each trial follows a fixed sequence.

| Time | Activity |
|------|----------|
| 0 – 0.5 s | Fixation Cross |
| 0.5 – 1.0 s | Visual Cue |
| 1.0 – 3.5 s | Inner Speech / Pronounced Speech / Visualization |
| 3.5 – 4.5 s | Rest Period |

A 15-second baseline recording is collected at the beginning of every session.

---

# Dataset Organization

The dataset follows the **Brain Imaging Data Structure (BIDS)** format.

Each participant folder contains:

- Raw EEG recordings (.bdf)
- Event files
- Channel information
- Electrode metadata
- Session information
- Participant metadata

The standardized structure simplifies loading the dataset using EEG analysis libraries such as MNE-Python.

---

# Why We Selected This Dataset

1. Multi-Session Recordings - Each participant was recorded across multiple sessions.

This allows analysis of how imagined speech patterns change over time and supports studies related to session variability.


2. High Temporal Resolution - The sampling rate of **1024 Hz** captures detailed temporal information, making it suitable for experiments that investigate how early a command can be recognized from EEG activity.


3. Verified Inner Speech - The inclusion of facial EMG recordings is one of the strongest features of this dataset.

It helps confirm that participants are genuinely performing inner speech rather than producing subtle facial movements that could influence the EEG signals.


4. Standardized Data Format - The BIDS organization reduces preprocessing effort and improves reproducibility across different research environments.

---

# Limitations

- Limited Vocabulary
- Small Number of Participants
- Controlled Recording Environment

---

# Relevance to Our Project

Due to :-

- Session-wise performance analysis
- Lightweight deep learning models
- Real-time Brain-Computer Interfaces

Its combination of multi-session recordings, high temporal resolution, and verified inner speech makes it an excellent benchmark for studying robust imagined speech decoding before moving toward more complex vocabulary-based systems.

---

# Reference

**Dataset**

Thinking Out Loud: An Open-Access EEG-Based BCI Dataset for Inner Speech Recognition

**Repository**

OpenNeuro (Dataset: ds003626)

**Publication**

Nieto, N., Peterson, V., Rufiner, H. L., Kamienkowski, J. E., & Spies, R.

*Thinking Out Loud: An Open-Access EEG-Based BCI Dataset for Inner Speech Recognition.*

Scientific Data, 9(1), 52, 2022.