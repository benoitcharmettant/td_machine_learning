from tools.features import *

class Log_ampl:
    n_outs = 1
    f = log_ampl
    f_names = [f.__name__]

class Log_mean:
    n_outs = 1
    f = log_mean
    f_names = [f.__name__]

class Mean:
    n_outs = 1
    f = mean
    f_names = [f.__name__]

class Log_energy:
    n_outs = 1
    f = log_energy
    f_names = [f.__name__]

class Kurtosis:
    n_outs = 1
    f = kurtosis
    f_names = [f.__name__]

class Log_kurtosis:
    n_outs = 1
    f = log_kurtosis
    f_names = [f.__name__]

class Skewness:
    n_outs = 1
    f = skewness
    f_names = [f.__name__]

class Log_variance:
    n_outs = 1
    f = log_variance
    f_names = [f.__name__]
    
class Zero_crossings:
    n_outs = 1
    f = zero_crossings
    f_names = [f.__name__]
    
class Frequency_bands:
    n_outs = 5
    f = frequency_bands
    f_names = ["band_delta", "band_theta", "band_alpha", "band_beta", "band_gamma"]
    
class Complexity:
    n_outs = 1
    f = complexity
    f_names = [f.__name__]
    
class Fft_agg:
    n_outs = 4
    f = fft_agg
    f_names = ["fft_centroid", "fft_variance", "fft_skew", "fft_kurtosis"]
    
class Entropy:
    f = entropy_c
    f_names = ["entropy"]
    n_outs = 1
    
class SEntropy:
    f = spect_entropy
    f_names = ["s_entropy"]
    n_outs = 1
    

