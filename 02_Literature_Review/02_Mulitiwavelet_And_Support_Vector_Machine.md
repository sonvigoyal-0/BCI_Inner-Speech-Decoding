# Enhancing the Classification Accuracy of EEG-Informed Inner Speech Decoder Using Multi-Wavelet Feature and Support Vector Machine

## Paper Info

| Field | Details |
|-------|---------|
| **Title** | Enhancing the Classification Accuracy of EEG-Informed Inner Speech Decoder Using Multi-Wavelet Feature and Support Vector Machine |
| **Authors** | Mokhles M. Abdulghani, Wilbur L. Walters, Khalid H. Abed |
| **Year** | 2024 |
| **Journal** | IEEE Access |
| **Volume/Article** | Volume 12 |
| **DOI** | [10.1109/ACCESS.2024.3474854](https://doi.org/10.1109/ACCESS.2024.3474854) |

## SUMMARY :-

This paper proposes an EEG-based inner speech decoding using **Multi-Wavelet Feature Extraction** with a **Support Vector Machine (SVM)** classifier to improve the accuracy of imagined speech classification.

In this paper there is no direct classification of raw EEG signals,instead the authors extract informative features using autoregressive modeling, Shannon entropy, and wavelet variance estimation. These features are then classified using SVM. The proposed approach was evaluated on two public EEG inner speech datasets and achieved **68.20% accuracy on Data 1** and **97.50% accuracy on Data 2**.

---

## Problem Statement :-

Individuals suffering from speech impairments are often unable to communicate despite having intact cognitive abilities. Existing communication systems are limited because they connects with physical speech or muscle movement.

The challenge addressed in this paper is:

> **Can silently imagined words (inner speech) be decoded directly from EEG signals with improved accuracy?**

---

## Research Objective :-

The primary objective of this work is to improve the classification accuracy of EEG-informed inner speech decoding by introducing a **Multi-Wavelet Feature Extraction** framework combined with a **Support Vector Machine (SVM)** classifier.
Also to maintain the accuracy using diffrent data.

---

## Proposed Approach :-

The proposed framework follows the pipeline:

Raw EEG Signals

↓

Signal Processing

↓

Multi-Wavelet Feature Extraction

- Autoregressive (AR)
- Shannon Entropy
- Wavelet Variance

↓

Feature Vector

↓

Support Vector Machine (SVM)

↓

Predicted Inner Speech Class

---

## Performance Summary :-

| Metric | Data 1 | Data 2 |
|---------|--------:|--------:|
| Accuracy | 68.20% | 97.50% |
| Precision | 68.22% | 97.73% |
| Recall | 68.20% | 97.50% |
| F1-Score | 68.21% | 97.61% |
| Macro AUC-ROC | 78.76% | 99.32% |

---

## Key Findings :-

- Multi-wavelet feature extraction effectively reduced EEG data dimensionality while preserving discriminative information.
- Support Vector Machine achieved strong classification performance using the extracted features.
- Data 2 has shown better accuracy over Data 1 due to better placement of elecrodes and high quality electrodes used
- using feature extractions like AR coefficients, Shannon entropy, and wavelet variance have improved feature representation.
- 10-fold cross-validation enhanced the reliability and generalization of the model.

---

# Limitations :-

Although the proposed method achieved high classification accuracy, several limitations remain:

- Focuses primarily on classification accuracy rather than real-time performance.
- No evaluation of inference latency.
- No cross-user adaptation analysis.
- No cross-session evaluation.
- Limited dataset size may affect generalization.

---

# Future Scope :-

Future work can focus on:

- Cross-subject generalization
- Real-time EEG decoding
- Lightweight deployment on embedded systems
- Larger and more diverse EEG datasets
- Deep learning-based feature learning
- Low-latency Brain-Computer Interface applications


---


## What I Learned :-

- Good preprocessing and feature extraction remains highly valuable especially when working with limited EEG dataset.
- Taking precautions sometime improve the performance more than switching to other DEEP LEARNING MODEL.
- Feature extraction reduces data size before classification, making traditional machine learning models more effective.

## Relevance to My Research :-

Paper has combined Multi-wavelet feature extraction with SVM which directly improves its accuracy and also due to placement of electrodes at Wernicke and Broca regions, which are considered good spots for better-quality inner speech-based EEG.

Hence,
This paper focuses on improving **classification accuracy**, whereas my research focuses on **low-latency EEG decoding**. The feature extraction strategy is valuable, but additional work would be needed to evaluate computational efficiency and real-time performance.

---
