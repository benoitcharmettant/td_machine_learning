import numpy as np

from tsfresh import extract_features
from tsfresh.feature_extraction import feature_calculators as fc
from tsfresh.feature_extraction.settings import MinimalFCParameters, EfficientFCParameters

from scipy.stats import skew

def log_ampl(x):
    return np.log(max(abs(x)))

def mean(x):
    return np.mean(x)

def log_mean(x):
    m = abs(np.mean(x))
    
    return np.log(m)
    

def log_energy(x):
    return np.log(fc.abs_energy(x))


def kurtosis(x):
    return fc.kurtosis(x)


def log_kurtosis(x):
    return np.log(fc.kurtosis(x))


def skewness(x):
    return skew(x)


def log_variance(x):
    return np.log(fc.variance(x))


def zero_crossings(x):
    return fc.number_crossing_m(x, 0)


def test(x):
    return [1, 2]