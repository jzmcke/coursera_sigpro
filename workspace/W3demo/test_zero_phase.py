import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)
shift = np.zeros(len(x))
shift[:8] = x[7:]
shift[8:] = x[:7]
X = fft(shift)
mX = abs(X)
pX = np.angle(X)