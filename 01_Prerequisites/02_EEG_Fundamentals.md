# EEG (ELECTROENCEPHALOGRAPHY)

## 1. How does EEG actually measure brain activity ?


1. Brain have 86 millions neuron (one single neuron is too weak for EEG to detect signal)

                                     |

2. Millions of neurons come together and generate tiny **Electric Feild**

                                     |

3. Now the signal reaches to the scalp and by that time it becomes very weak (in microvolt)

                                     |

4. EEG electrodes detect it (each electrodes measures the volt diffrence between brain region)

                                     |

5. EEG machine converts time voltage into graph known as **EEG Signals**

                                     |



## 2. ELECTRODES
 
CHANNEL - EEG signals recorded by electrode is known as channel 
EEG caps -> 64 electrodes -> means 64 recording of signals -> means 64 channels

10-20 System - international system which is standard method for placing the elctrodes to get same output 


**Electrode Names**

| Electrode | Brain Region | Function |
|-----------|--------------|------------------|
| **Fp** | Frontal Pole | Eye movement (EOG artifacts), attention |
| **F** | Frontal | Planning, decision making, cognitive functions |
| **C** | Central | Motor control, motor imagery |
| **P** | Parietal | Sensory processing, spatial perception |
| **O** | Occipital | Visual processing (SSVEP) |
| **T** | Temporal | Hearing, language processing |

## 3. NUMBERS
 - Odd no. -> means left hemisphere in brain
 - Even no. -> means right hemisphere in brain

  example :- (Electrodes)

            **Motor Imagery**
                  C4 - right motor cortex
                  C3 - left motor cortex
                  Cz - central part of motor cortex

            **SSVEP**
                  O1 - left visual cortex
                  O2 - right visual cortex
                  Oz - centre

            **P300**
                  Pz
                  Cz
                  Fz
                

## 4. PARADIGM
A task goven to a participant 

          ** Paradigm **
                     
                     1.Motor Imagery :-
                    - Imagining the movement without actually performing it 
                    - The muscles are not moving in actual but the brain behaves as if it moving or preparing to move
                    - Motor cortex get actives while imagining the movement and EEG detects
                    - Highly used in paralysis becuase muslces cant move but by imaganing the help can be detected
                    - But motor imagery is hard to detect becuase it's frequency vaires person to person

                     2.SSVEP:-
                    - Steady state visual envoked potential
                    - If we look continously at a flashing object our virtual cortex produces EEG signal at same frequency as flashing light 
                    - **ADVANTAGE**
                                 - High accuracy
                                 - fast response
                                 - easy to classify
                    - **DISADVANTAGE**
                                 - cause eye fatigue
                                 - need constant visual attention
                        
                          
                     3.P300:-
                    - Detect a rare target stimulus (Partial cortex)
                    - 300 means - it usually appears about 300 millisecond after the target stimulus
                    - example :-
                                u have to count G appearing -> whenever G appears brain active and P300 appears
                    - use in spellers , comm. system , cursor control


                     4.Resting State - To relax

What we get to know ?
- which brain regin get active 
- which electrode to be used
- which ML model would work better 


Means future all work will depend on task given to the user means paradigm
                  
## 5. BRAIN WAVES
Means when multiple neurons come together , the electrical activity produces known as **Brainwaves**

| Brain Wave | Frequency | Brain State |
|------------|-----------|-------------|
| **Delta (δ)** | 0.5–4 Hz | Deep sleep |
| **Theta (θ)** | 4–8 Hz | Drowsiness, meditation, light sleep (deep thoughts) |
| **Alpha (α)** | 8–13 Hz | Relaxed, eyes closed (calm state) |
| **Mu (μ)** | 8–13 Hz | Motor imagery and motor cortex activity |
| **Beta (β)** | 13–30 Hz | Active mind, movement, concentration |
| **Gamma (γ)** | >30 Hz | Higher cognition , attention (hard to recognize wave) |

- Mu is the most important for BCI 
     - It is present at sensorimotor cortex of brain region
     - Task is movement
     - Mu changes during motor imagery

- **Frequency** is important for BCI because the signal is recognized between 8-30 hz which directly helps in concluding that **Mu** and **Beta** were active hence **motor imagery**


## ERP (EVENT RELATIVE POTENTIAL) :-
    The temporary change in EEG signal due to any event occured is ERP 
    Example - staring at a screen -> red light comes -> brain effect -> EEG detect 
    then that changes in EEG is ERP


## ERD and ERS
    (EVENT RELATED DESYNCHRONIZATION) :-
    Means brain wave power decreases after an event 
    Event means imaganing any movement which drecreases MU power
    hence ERD decreases

    (EVENT RELATED SYNCHRONISATION):-
    Means after the completion of any task the brain comes to rest 
    hence MU power increases


## EEG ARTIFACTS :-
    Unwanted signals that mixed with EEG [as it records everything not just brain activity]
    Artifacts generated by blinking , heartbeat , eye movement

    **EOG(ELECTROOCULOGRAM)** is type of artifact which is generated due to eye movement like blinking or left right looking


## SNR (SIGNAL TO NOISE RATIO):-
    It tells how much useful brain signal exist compared to unwanted noise
    Hence high SNR means better EEG quaity
    To remove artifacts :-
              Band pass filter 
              Notch filter
              ICA(independent component analysis)



