# LPC-of-Speech-Signal
LPC is a very powerful speech analysis technique used to estimate basic speech parameters. It provides extremely accurate estimation of speech parameters.
In LPC, Speech Signals can be approximated as linear combination of past samples by minimizing the error. This has been done by minimizing the sum of squared differences between the actual speech samples and the predicted ones
LPC is useful and most powerful for audio and speech signal processing and also it reduces the bit rate. It is used as a form of voice compression by phone companies for example GSM standard.
Firstly we have plotted the speech signal for very large samples, then we have divided that speech signal into Hamming window frames. Now for each frames we have performed LPC analysis and plotted DFT and LPC spectrum of it.
Atlast we have detected the envelope of DFT spectrum and generated that envelope on the spectrum. 
