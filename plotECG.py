#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 07:35:49 2023

@author: aleckorsah
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.datasets import electrocardiogram
from scipy.signal import find_peaks
x = electrocardiogram()[9000:11000]
peaks, _ = find_peaks(x, distance=120,height=.5)
plt.plot(x, label = "ECG")
plt.plot(peaks, x[peaks], "x", label = "Peaks")
plt.xlabel("Time (s)",)
plt.ylabel("Voltage (mV)")
plt.title("section 1")
plt.legend()
plt.show()