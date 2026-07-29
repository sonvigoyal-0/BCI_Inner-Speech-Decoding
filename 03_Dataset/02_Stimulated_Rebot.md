# Dataset 2: EEG Data Recorded During Spoken and Imagined Speech Interaction with a Simulated Robot


# Overview

This dataset contains EEG recordings gathered while volunteers interacted with a simulated robot using both **spoken** and **imagined speech** commands.

In contrast to conventional motor imagery datasets, the volunteers generated meaningful command words such as movement and interaction commands. This makes the dataset useful for imagined speech decoding and command-based BCI research.

The dataset is publicly available through Zenodo and was introduced to analyse how overt speech can support the training of silent speech decoding models.

---

# Dataset Summary

| Parameter | Details |
|-----------|---------|
| Number of Participants | 15 Healthy Subjects |
| EEG Channels | 64 |
| Recording Sessions | 1 Session (4 Experimental Blocks) |
| Vocabulary Size | 5 Command Words |
| Total Trials | Approximately 800 per participant |
| Recording Paradigm | Spoken and Imagined Speech |
| Dataset Source | Zenodo |
| Research Area | Imagined Speech BCI |

---

# Hardware and Recording Setup

The experiment was executed using a **64-channel EEG acquisition system** whereas participants operated with a simulated robot displayed on a monitor.

Volunteers remained seated during the experiment and generated spoken or imagined speech commands based on visual guidelines.

The study alternated between overt speech and imagined speech blocks to reduce fatigue-related effects and maintain consistent attention throughout the recording.

---

# Experimental Design

The experiment contains four recording blocks:

1. Overt Speech
2. Imagined Speech
3. Overt Speech
4. Imagined Speech

This alternating design minimizes the possibility that the model learns differences caused by fatigue or changing mental states replacing actual speech-related brain activity.

---

# Target Commands

Participants generated five command words throughout the experiment.

- Left
- Right
- Up
- Pick
- Push

These commands represent practical robot navigation and interaction tasks, making the dataset suitable for command-based BCI systems.

---

# Trial Structure

Each trial used the same sequence.

- A fixation cross was visible for 2 seconds.
- During this period, the volunteer either spoke or silently imagined the displayed command.
- After the trial ended, the robot state on the screen was updated before the next instruction was presented.

The consistent timing makes the dataset suitable for studying different decision windows during imagined speech decoding.

---

# Dataset Organization

The Zenodo obtain is organized participant-wise.

Each participant folder contains:

- EEG recordings
- Event markers
- Trial labels
- Experimental condition information (spoken or imagined speech)

The event markers allow precise detection of the 2-second imagined speech windows for further analysis.

---

# Why We Selected This Dataset

This dataset aligns well with the objectives of our research for several reasons.

1. **Command-Based Imagined Speech** - In contrast of generic motor imagery tasks, the dataset focuses on meaningful command words.

This allows the model to learn neural activity associated with linguistic intention rather than simple limb movement imagination.


2. **Suitable for Low-Latency Experiments** - Every trial has a fixed duration of two seconds.

This makes it possible to study how early the intended command can be identiified by testing shorter time windows such as:

- 250 ms
- 500 ms
- 750 ms
- 1000 ms

These experiments are directly relevant to low-latency BCI development.

---

3. **High-Density EEG Recording** - The use of 64 EEG channels provides rich spatial information that can help in analyse speech-related brain activity more effectively than low-density systems.


4. **Balanced Experimental Design** - Both spoken and imagined speech were collected under the same guidelines.

Although our project focuses on imagined speech, the spoken speech recordings may also support future studies including transfer learning or representation learning.

---

# Limitations

Although the dataset is valuable, it also has several practical limitations.

1. **Limited Vocabulary** - Only five command words are included.

This restricts research on large-vocabulary imagined speech decoding.


2. **Single Recording Session** - Each volunteer was recorded during a single session.

In result, the dataset is less suitable for analyzing long-term cross-session robustness.


3. **No Additional Muscle Monitoring** - The dataset does not explicitly include EMG recordings to verify the complete absence of facial muscle activity during imagined speech.

This makes it difficult to completely rule out subtle muscle activation.



---

# Relevance to Our Project

This dataset can support various aspects of our research, involving:

- Lightweight neural network evaluation
- Latency versus accuracy analysis

Although it is not designed for cross-session evaluation, it provides a strong benchmark for analyzing how quickly imagined speech can be recognized from short EEG windows.

---

# Reference

**Dataset**

EEG Data Recorded During Spoken and Imagined Speech Interaction with a Simulated Robot

**Repository**

Zenodo

**Associated Publication**

Rekrut, M., Selim, A. M., & Krüger, A.

*Improving Silent Speech BCI Training Procedures Through Transfer from Overt to Silent Speech.*

IEEE International Conference on Systems, Man, and Cybernetics (SMC), 2022.