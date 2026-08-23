# Dataset 3: EEGIS – Electroencephalogram Imagined Speech Dataset

---

# Overview

The EEGIS dataset is a public imagined speech EEG dataset developed for Brain-Computer Interface (BCI) research. It contains EEG recordings collected while participants silently imagined a set of predefined command words without producing any actual speech.

The dataset is designed for command-based imagined speech decoding and provides a lightweight EEG setup that is suitable for developing practical and portable BCI systems.

---

# Dataset Summary

| Parameter | Details |
|-----------|---------|
| Number of Participants | 10 Healthy Subjects |
| Age Group | 20–30 Years |
| EEG Device | Emotiv EPOC+ |
| EEG Channels | 14 |
| Sampling Rate | 128 Hz |
| Vocabulary | 8 Spanish Command Words + Rest State |
| Total Classes | 9 |
| Data Format | CSV Files |
| Dataset Source | Mendeley Data |

---

# Hardware Configuration

The EEG recordings were collected using the **Emotiv EPOC+** wireless headset.

The headset records brain activity from **14 EEG channels**, providing a lightweight and portable acquisition setup that is closer to real-world wearable BCI systems than high-density laboratory equipment.

---

# Experimental Design

Volunteers were instructed to silently imagine predefined command words without speaking or making intentional facial movements.

The experiment consists of:

- One resting-state class
- Eight imagined speech command classes

Each EEG trial was segmented into **1-second windows**, making the dataset convenient for machine learning experiments.

---

# Vocabulary

The dataset contains nine classes.

- Rest
- Eight imagined Spanish command words

The command-based vocabulary makes the dataset suitable for discrete imagined speech classification rather than continuous sentence decoding.

---

# Dataset Organization

The dataset is organized into separate folders according to frequency bands.

The main directory contains:

- Raw_Data
- Delta_Band
- Theta_Band
- Alpha_Band
- Beta_Band
- Gamma_Band

Inside each folder:

- Individual class directories
- One CSV file per EEG trial

Each CSV file stores a **14 × 128 EEG matrix**, representing one second of multichannel EEG data.

The organized folder structure simplifies data loading for machine learning applications.

---

# Why We Selected This Dataset

1. **Lightweight EEG Acquisition** - The recordings were collected using only **14 EEG channels**, making the dataset representative of practical wearable BCI systems.


2. **Portable Hardware** - The Emotiv EPOC+ headset is widely used in portable EEG research.

This makes the dataset useful for examining computationally efficient decoding methods.


3. **Simple Data Organization** - Each trial is already segmented and stored individually.

This reduces preprocessing effort and allows faster experimentation during model development.

---

4. **Frequency-Specific Data** - The availability of separate frequency-band folders allows researchers to analyze different EEG rhythms without manually organizing the recordings.

---


# Limitations

1. **Limited Vocabulary** - Only a small set of imagined command words is available.

This limits research on large-vocabulary or continuous imagined speech decoding.


2. **Low Spatial Resolution** - Using only 14 EEG channels reduces hardware complexity but also provides less spatial information than medical-grade EEG systems.


3. **Consumer-Grade Hardware** - The Emotiv headset is convenient for portable applications but generally provides lower signal quality compared to research-grade EEG systems.


4. **Controlled Recording Conditions**


---

# Relevance to Our Project

The EEGIS dataset is well suited for investigating:

- Lightweight imagined speech decoding
- Low-latency EEG classification
- Portable Brain-Computer Interfaces
- Edge AI deployment
- Command-based neural decoding

Although the vocabulary is narrow, it provides an outstanding benchmark for evaluating computationally efficient imagined speech models before extending to more complex language tasks.

---

# Reference

**Dataset**

EEGIS – Electroencephalogram Imagined Speech Dataset

**Repository**

Mendeley Data

**Hardware**

Emotiv EPOC+

**License**

Available through Mendeley Data under the dataset's published license.