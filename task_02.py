#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import numpy as np


def numpy_task02(themean, stddev, numvals):
    """Returns list of normally-distributed random numbers
    Can be useful for getting a snapshot of the distribution
    within a population."""
    rdmsample = np.random.normal(themean, stddev, numvals)
    return rdmsample