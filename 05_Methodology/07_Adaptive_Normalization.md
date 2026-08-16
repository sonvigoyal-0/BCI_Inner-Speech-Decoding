# Architecture Notes

These notes outline a dual-stage, edge-optimized architecture for asynchronous Brain-Computer Interfaces (BCIs), aiming for ~90% accuracy under a 200ms latency budget .

##  Methodology I: Adaptive Feature Normalization
Raw EEG signals are inherently unstable due to electrode impedance shifts, sweat, and user fatigue. The system must anchor these signals to a stable baseline.

### Z-Score Transformation & EMA
*   **Initial Baseline:** A 30–60 second "eyes-open rest" period captures the initial mean (mu) and standard deviation (sigma) of the user's brainwaves .
*   **Continuous Updates:** To handle slow drift throughout the day, the system uses an Exponential Moving Average (EMA) to incrementally update the baseline during idle periods, keeping the signal stable and zero-centered .

### Relative Band Power Ratios
*   Instead of looking at absolute power (which fluctuates wildly), the system calculates relative band power ratios R_{band} = P_{band} / P_{total}.
*   If hardware gain shifts, the ratio between frequencies (e.g., Alpha vs. Beta) remains preserved, isolating the true neural intent from acquisition noise.

## Methodology II: Evidence Accumulation Models
To prevent false alarms in a continuous data stream, the system uses "evidence accumulation," building confidence over time rather than making instant guesses .

### Cumulative Sum (CUSUM)
*   **How it Works:** A lightweight, math-based change detection formula. It includes a slack parameter for expected shift magnitude and a threshold that triggers the "brain switch" .
*   **The Advantage:** It uses a  operator to prevent negative evidence from building up during idle states, allowing it to trigger instantly when genuine intent begins . It is highly suited for edge devices .

### Drift-Diffusion Model (DDM)
*   **How it Works:** A more complex, parametric model (a leaky stochastic accumulator). It tracks accumulation speed (Drift Rate) against a decision threshold .
*   **The Advantage:** It features a "Leak Term" (lambda) that acts as a safety valve, pulling the accumulator back to zero during noisy idle periods to prevent false positives. 
*   *Note: DDM is computationally heavier than CUSUM due to stochastic simulation overhead* .

## 5. Critical Implementation Takeaways
1.  **Z-Score + EMA is Mandatory:** It is the only way to handle within-session signal drift .
2.  **Detection Before Decoding:** Stage 1 (CUSUM/DDM) must act as a strict gatekeeper for Stage 2 (EEGNet). This saves battery and stops false positives.
3.  **Edge-First Profiling:** Classification accuracy does not matter if the model takes longer than 200ms to run on the Jetson TX2 .
4.  **LOSO Validation:** All models must be validated using Leave-One-Subject-Out cross-validation to prove they work across different humans with different brain patterns 