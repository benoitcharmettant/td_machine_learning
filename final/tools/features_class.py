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

    
def test_func(x):
    return [1, 2]

class Test:
    n_outs = 2
    f = test_func
    f_names = ['fourier_alhpa', 'f_2']