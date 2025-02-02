import matplotlib.pyplot as plt
import numpy as np
from smstools.models import utilFunctions as UF
from smstools.models import dftModel as DF
(fs, x) = UF.wavread('../../../sounds/sine-440-490.wav')
w = np.hamming(3528)
N = 16384
pin = int(.11*fs)
x1 = x[pin:pin+w.size]
mX, pX = DF.dftAnal(x1, w, N)

plt.figure(1, figsize=(9.5, 5))
plt.subplot(311)
plt.plot(np.arange(pin, pin+w.size)/float(fs), x1, 'b', lw=1.5)
plt.axis([pin/float(fs), (pin+w.size)/float(fs), min(x1)-.01, max(x1)+.01])
plt.title('x (sine-440-490.wav), M=3528')

plt.subplot(3,1,2)
plt.plot(fs*np.arange(mX.size)/float(N), mX, 'r', lw=1.5)
plt.axis([100,900,-85,max(mX)+1])
plt.title ('mX, N=16384')

plt.subplot(3,1,3)
plt.plot(fs*np.arange(pX.size)/float(N), pX, 'c', lw=1.5)
plt.axis([100,900,7,32])
plt.title ('pX')

plt.tight_layout()
plt.savefig('two-sines-spectrum-2.png')
plt.show()
