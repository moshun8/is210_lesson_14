#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""


import numpy as np


def numpy_task03(txtfile):
    """Returns tuple of txt file mean and standard deviation"""
    try:
        txtarray = np.loadtxt(txtfile)
        arrmean = int(np.mean(txtarray))
        stddev = int(np.std(txtarray))
        return (arrmean, stddev)
    except Exception:
        raise