import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft
import sys
import os
import math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as uf


(fs, x) = uf.wavread('../../sounds/soprano-E4.wav')

M=501
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

x1 = x[5000:5000+M] * np.hamming(M)

N=1024
fft_buffer = np.zeros(N)
fft_buffer[:hM1] = x1[hM2:]
fft_buffer[N-hM2:] = x1[:hM2]

X = fft(fft_buffer)
mX = 20*np.log10(abs(X))
pX = np.unwrap(np.angle(X))