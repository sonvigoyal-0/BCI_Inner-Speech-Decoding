## BCI PIPELINE

                                    Human
                                      ⇩
                                Signal Acquisation
                                      ⇩
                                Preprocessing
                                      ⇩
                                Feature Extraction
                                      ⇩
                                Feature Selection
                                      ⇩
                                Classification
                                      ⇩
                                   Descision
                                      ⇩
                                    Feedback



1. Signal Acquisation - collecting signals from brain

2. Preprocessing - cleaning raw EEG signals

3. Feature Extraction - extraction or creates useful information from raw EEG signal. Common feature extractions :-
                                -PSD
                                -FFT
                                -Wavelet
                                -CSP

4. Feature Selection - now out of 500 features which were extracted some of important features will be selected. This provides 
                                -High accuracy
                                -Low latency
                                -Less computation

5.  Classification - this is a ML model where classifier predicts whether its a left hand or right hand. Common classifiers :-
                                -SVM
                                -LDA
                                -CNN
                                -RNN
                                -KMM
                                -Random forest

6. Descision - As classifier had decided which hand, so accordingly the curson on computer will react

7. Feedback - Its a final goal where user can see the working screen due to its thought