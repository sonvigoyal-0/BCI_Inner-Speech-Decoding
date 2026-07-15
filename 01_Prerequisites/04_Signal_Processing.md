# SIGNAL PROCESSING
Working beofre classification(ML Model)


                                     Raw EEG
                                        ⇩
                                     Filtering
                                        ⇩
                                       ICA (preprocessing)
                                        ⇩
                                       FFT (feature ext)
                                        ⇩                            ( or wavelet )
                                       PSD
                                        ⇩
                                       CSP
                                        ⇩
                                   Classification

                            

## FILTERING :-
Keeping useful frequency and removing unwanted freq

**METHODS FOR REMOVING NOISE FROM THE SIGNAL

                1. BAND PASS FILTER - Where a fixed amount of freq is allowed rest all are cancelled
                                    - Hence it keeps fixed freq range
                
                2. NOTCH FILTER - Removes power interfrence
                                - Means it removes one specific freq 
                                - use when India has 50hz and USA has 60hz so to remove electicity noise 

                3. ICA (INDEPENDENT COMPONENT ANALYSIS) - this method separates mixed EEG signals into independent sources.
                               - So now we can directly remove eye moevement or any ohter noise and keep the brain signals

                4. FFT (FAST FOURIER TRANSFORM) - in this method the signal is converted from time domain to freq domain
                               - Now by freq changing we can see which siganl is need and which have to be removed

                5. PSD (POWER SPECTRAL DENSITY) - This tells how much power exist at each freq 
                               - example - 20 hz -> high freq
                               - As motor imagery changes power before and after of imagination so PSD helps
                               - As it tells the power/energy in high and low form so a pattern can be formed and that pattern is used by classifers


## WAVELET TRANSFORM :-
- Brain or EEG signal changes every second and FFT method only tells about freq  but not at what time hich freq
- This method tells that which freq occured and at what time

## CSP (COMMON SPATIAL PATTERN) :-
- CSP find the electrodes which contains the most info and best in distinguishing between 2 choices
- So it is best for classifier accuracy 

## EPOCHING :-
- Dividing your long EEG signal into small small peices like divind 30 min into 2-2 sec is known as epoch
- In machine learning we require patterns and from small signals we can form pattern so epoch healp

## WINDOWING :-
- A window is a time interval selected for analysis
- 