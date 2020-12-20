import numpy as np

from tsfresh import extract_features
from tsfresh.feature_extraction import feature_calculators as fc
from tsfresh.feature_extraction.settings import MinimalFCParameters, EfficientFCParameters

from scipy.stats import skew

from tools.freq import get_mean_freq_bands

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

def frequency_bands(x):
    return get_mean_freq_bands(x)

def complexity(x):
    return cid_ce(x, True)

def fft_agg(x):
    param = [{"aggtype": "centroid"}, {"aggtype": "variance"}, {"aggtype": "skew"}, {"aggtype": "kurtosis"}] 
    return list(dict(fc.fft_aggregated(x, param)).values())



def test(x):
    return [1, 2]