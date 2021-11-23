import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import librosa
import scipy 

input_speech,fs=sf.read("D:\IIT MANDI\Sem 1\CS571 Programming Practicum\Project\should.wav")
print('sampling rate', fs)
ln = len(input_speech)
n=np.linspace(0,ln-1,ln)
plt.figure(1)
plt.plot(n,input_speech)
plt.legend(['plot of sample'])
plt.xlabel('sample')
plt.ylabel('amplitude')
plt.title("should.wave signal")
plt.grid()

def enframe(x, winsize, hoplength, fs, wintype):
    hpln = int(fs*hoplength*0.001)
    wnsz =int(fs*winsize*0.001)
    temp = wnsz - (len(x)%hpln)
    z = np.pad(x,(0,temp),'constant')
    if wintype == 'hamm':
        win =np.hamming(wnsz)
    elif wintype=='rect':
        win=np.ones(wnsz)
    frame =[]
    l =len(x)
    for i in range(0,l,hpln):
        a = z[i:i+wnsz]*win
        frame.append(a)
    return(frame)

windowdata = enframe(input_speech, 30 ,15 ,fs, 'hamm')  

S=[]
A=[]
f=fs/1000

## Spectrum of one frame
for i in  windowdata:
    a=np.log10(np.abs(np.fft.fft(i)))
    n1=np.linspace(0,len(a)-1, len(a))
    a=a[0:len(a)//2]
    freq=n1*(f/len(n1))
    freq=freq[0:len(freq)//2]
    A.append(a)
    S.append(freq)
def autocorr(i):
    result=np.correlate(i,i, mode='full')
    return result[int(result.size/2):]

x=0
xs = windowdata[0]
b = librosa.lpc(xs,20)
im = np.ones(300)
w,h = scipy.signal.freqz([1],b, 150)
plt.figure(2)
plt.subplot(2,1,1)
plt.legend(['DFT spectrum'])
plt.xlabel("frequency in π")
plt.ylabel("log magnitude")
plt.title("DFT spectrum")
plt.plot(S[x],A[x],color="red")
z = np.log10(np.abs(h))
plt.subplot(2,1,2)
plt.title("LPC Envelope")
plt.legend(['LPC Envelope'])
plt.plot(S[x],z,color="green")
