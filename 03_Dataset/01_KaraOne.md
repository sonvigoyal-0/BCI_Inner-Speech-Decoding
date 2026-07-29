# Dataset 1 - KaraOne – EEG Dataset for Imagined and Articulated Speech Recognition

---

## Overview

Karaone is one of the most used public dataset for imagined speech BCI research. In this dataset it contatins EEG recordings which are collected when participants both imgined speaking and actually spoke a set of predefined phonemes and words.

Unique art of this dataset is it includes facial and audio recordings using **Microsoft Kinect Sensor. These additional recordings help to verify that participants were not unintentionally moving their speech muscles durin the imagined speech task, making the dataset valuable for silent speech research.

The dataset was developed by the University of Toronto and has become a common benchmark for imagined speech decoding studies.

---

# Dataset Summary

| Parameter | Details |
|-----------|---------|
| Number of Participants | 14 (12 usable after quality control) |
| EEG System | Neuroscan Quick-Cap |
| EEG Channels | 62 EEG + 4 EOG |
| Sampling Rate | 1000 Hz |
| Recording Duration | Approximately 30–40 minutes per participant |
| Recording Sessions | Single Session |
| Vocabulary | 7 Phonemes + 4 English Words |
| Total Classes | 11 |
| Additional Sensors | Microsoft Kinect (Audio + Facial Tracking) |
| Data Format | MATLAB (.mat) |

---

# Hardware Configuration

The EEG recordings were acquired using a **64-channel Neuroscan Quick-Cap** connected to a **SynAmps RT amplifier**.

To complement the EEG recordings, a **Microsoft Kinect v1.8** sensor continuously captured facial movements and speech audio throughout the experiment.


The combination of EEG and Kinect recordings helps in monitoring the participants behaviour during both imagined and overt speech tasks.

---

# Experimental Design

Each trial followed the same sequence of events.

1. **Rest** - Participants first remained relaxed to establish a resting state before each trial.


2. **stimulus** - A text prompt appeared on the screen, followed by the corresponding audio pronunciation.

Participants were given a short preparation period before beginning the task.


3. **Imagined Speech** - Participants silently imagined pronouncing the displayed phoneme or word without producing any sound.

No intentional speech or articulation was allowed during this stage.

---

4. **Overt Speech** - Immediately after the imagined speech period, participants pronounced the same prompt aloud.

The spoken recordings were captured together with facial movements using the Kinect system.

---

# Vocabulary

The dataset contains eleven target classes.

1. **Phonemes** :-

- /iy/
- /uw/
- /piy/
- /tiy/
- /diy/
- /m/
- /n/

2. **Words** :-

- Pat
- Pot
- Knew
- Gnaw

The inclusion of both phonemes and complete words allows researchers to investigate speech decoding at different linguistic levels.

---

# Trial Structure

Each trial consists of four consecutive stages.

| Stage | Description |
|-------|-------------|
| Rest | Baseline relaxation period |
| Stimulus | Visual and auditory presentation of the target |
| Imagined Speech | Silent mental pronunciation |
| Overt Speech | Spoken pronunciation recorded using EEG and Kinect |

This structured protocol provides paired imagined and spoken speech data for every prompt.

---

# Dataset Organization

The dataset is organized by participant.

Each participant folder contains:

- Raw EEG recordings
- Preprocessed MATLAB files
- Trial labels
- Event information
- Kinect audio recordings
- Facial tracking data

The provided files allow researchers to work directly with either raw recordings or preprocessed EEG signals.

---

# Why We Selected This Dataset

KaraOne offers several attributes that make it valuable for imagined speech research.

1. **Rich Speech Representation** - 

In contrast to motor imagery datasets, KaraOne addresses speech-related brain activity using both phonemes and meaningful English words.

This makes it suitable for exploring neural decoding of language rather than simple movement intentions.

2. **High Temporal Resolution** - The recordings were collected at **1000 Hz**,delivering detailed temporal information for analyzing how speech-related brain activity evolves over time.

3. **Multimodal Recording** - 

The parallel recording of EEG, speech audio, and facial movements helps improve confidence that the imagined speech trials contain limited unintended articulation.

4. **Benchmark Dataset** - KaraOne has been frequently used in imagined speech research and is frequently referenced when evaluating new EEG decoding methods.

**Its popularity makes it a useful benchmark for comparing future models**.

---


# Limitations

Although KaraOne is widely used, it also has several practical limitations such as :-

1. **Limited Vocabulary** - The dataset contains a small set of phonemes and words. Also hard for complex language or long speech 


2. **Single Recording Session** - Each participant was recorded during only one session. Which results in dataset which is not well suited for evaluating long-term session variability.



3. **Small Participant Group** - Only twelve participant recordings cn be used after quality control. This limits large-scale evaluation of subject-independent models.


4. **MATLAB-Based Format** - The dataset is distributed primarily in MATLAB format rather than BIDS. Also preprocessing may be required before using modern EEG analysis libraries.


# Relevance to Our Project

KaraOne closely matches the objectives of our research because it focuses on imagined speech rather than motor imagery.

The dataset can helps in :-

- Low-latency imagined speech decoding
- Neural word recognition
- Lightweight deep learning models
- Thought-to-text systems
- Benchmark evaluation of new decoding approaches

Although the vocabulary is limited, it provides a reliable foundation for developing and evaluating imagined speech decoding methods before extending the work to larger vocabularies.
Also it worked on main Problem Statement.

---

# References :-

**Dataset**

KaraOne: An EEG Dataset for Imagined and Articulated Speech

**Source**

University of Toronto

**Publication**

Zhao, S., & Rudzicz, F.

*Classifying Phonological Categories in Imagined and Articulated Speech.*

IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2015.