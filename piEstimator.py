#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:03:22 2023

@author: aleckorsah
"""

import numpy as np

def piEstimator(n):
    tol = 1e-5
    pi_Est = 0.0
    true_pi = np.pi
    truePctRelError = 0.0

    for k in range(1, n):
        term = (-1) ** (k + 1) / (2 * k - 1)
        pi_Est += term

    pi_Est *= 4
    truePctRelError = abs((pi_Est - true_pi) / true_pi) * 100

    return pi_Est, truePctRelError

print(piEstimator(3))