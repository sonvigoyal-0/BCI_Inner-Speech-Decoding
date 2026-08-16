# Notes: Self-supervised Learning for Electroencephalogram (A Systematic Survey)
(Paper was read to understand this methodology)

## 1. Paper Overview
*   **The Core Problem:** Deep learning models for EEG analysis are severely constrained by the scarcity of labeled samples and the significant variability of EEG signals across different subjects.
*   **The SSL Solution:** Self-Supervised Learning (SSL) extracts effective representations from unlabeled EEG data by utilizing well-designed pretext tasks to generate pseudo-labels. 
*   **Significance:** SSL reduces the reliance on costly, expert-annotated data while improving model generalization across various downstream tasks.

## 2. Taxonomy of SSL Methods for EEG
The authors categorize EEG-based SSL frameworks into four primary groups :-

### A. Predictive-based SSL
These methods create classification pretext tasks to predict discrete pseudo-labels. 
*   **Spatial Predictive:** Extracts channel correlation and brain structure features using tasks like EEG channel jigsaw, channel correlation prediction, and replace discriminative tasks.
*   **Temporal Predictive:** Captures sequential dependencies and temporal correlations via tasks like relative positioning, temporal shuffling, time-shift prediction, and temporal trend prediction.
*   **Transformation Predictive:** Enhances temporal-frequency aligned features by having the model recognize specific augmentations (e.g., stopped band prediction, scaling, flipping, and adding noise) applied to the EEG signal.

### B. Generative-based SSL
These approaches rely on reconstructing masked or transformed samples to learn fine-grained contextual correlations.
*   **Temporal Reconstruction:** Uses an encoder-decoder architecture (like Masked Autoencoders or MAE) to reconstruct original or masked temporal EEG signals and embeddings, effectively preserving critical sequential information.
*   **Multi-domain Reconstruction:** Extends reconstruction across temporal, spatial, and frequency domains simultaneously (e.g., extracting integrated features through Continuous Wavelet Transform and reconstructing the 3D matrix) to generate more general representations.

### C. Contrastive-based SSL
This is the most widely used technique, focusing on pulling positive pairs (similar samples) closer in the representation space while pushing negative pairs (dissimilar samples) apart.
*   **Contrastive Predictive Coding (CPC):** Uses contextual windows to accurately predict future representations, extracting invariant temporal features.
*   **Transformation Contrastive:** Applies augmentations (like cropping, scaling, or time shifting) to generate positive/negative pairs, forcing the model to learn invariant signal features.
*   **Spatial Contrastive:** Utilizes channel-level spatial augmentations (e.g., spatial shuffling or graph-based node dropping) to understand the spatial distribution of EEG channels across the brain.
*   **Composite Contrastive:** Performs cross-view and cross-domain contrastive learning (e.g., contrasting time and frequency domain representations) to extract more expressive, complex signal knowledge.
*   **Task-oriented Contrastive:** Creates highly specific frameworks, such as contrasting EEG signals with visual images or speech, to solve specialized decoding tasks.

### D. Hybrid SSL
*   Combines multiple pretext tasks (e.g., integrating predictive and contrastive tasks) to jointly train the model using multi-task loss functions.
*   This allows the shared encoder to extract richer representations containing multi-dimensional knowledge, though it requires careful task selection to avoid gradient interference.

## 3. Future Research Directions
The authors outline several potential directions for the future of SSL in EEG analysis :
*   **Signal-oriented Pretext Tasks:** Moving beyond standard image/text adaptations to design pretext tasks tailored specifically to EEG's unique spatial-temporal-frequency characteristics.
*   **Knowledge-driven SSL:** Integrating formal neural and clinical knowledge into the SSL framework to improve the interpretability and generalizability of the learned representations.
*   **Graph-based SSL:** Utilizing Graph Neural Networks (GNNs) to better model the inherent topological connectivity among brain regions and electrodes.
*   **SSL for Heterogeneous EEG:** Developing frameworks capable of jointly pre-training on highly varied datasets (different devices, sampling rates, and subjects) to build universal foundational models.
*   **Multi-modal SSL:** Combining unlabeled EEG data with other physiological signals (like ECG or EMG) to tackle highly complex downstream tasks.
