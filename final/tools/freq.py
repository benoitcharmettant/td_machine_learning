import numpy as np

def get_mean_freq_bands(x):
    
    fft_vals = np.absolute(np.fft.rfft(x))
    fft_freq = np.fft.rfftfreq(len(x), 1.0/50)

    eeg_bands = {'Delta': (0, 4),
                 'Theta': (4, 8),
                 'Alpha': (8, 12),
                 'Beta': (12, 30),
                 'Gamma': (30, 45)}

    # Take the mean of the fft amplitude for each EEG band
    eeg_band_fft = dict()
    for band in eeg_bands:  
        freq_ix = np.where((fft_freq >= eeg_bands[band][0]) & 
                           (fft_freq <= eeg_bands[band][1]))[0]
        
        if len(fft_vals[freq_ix]) == 0:
            mean = 0
        else:
            mean = np.mean(fft_vals[freq_ix])
        
        eeg_band_fft[band] = mean
        
    return list(eeg_band_fft.values())

# TODO: Mettre en commun le calcul des bandes pour l'extraction de feature
def get_mean_alpha(x):
    return np.log(get_mean_freq_bands(x)['Alpha'])

def get_mean_beta(x):
    return np.log(get_mean_freq_bands(x)['Beta'])

def get_mean_delta(x):
    return np.log(get_mean_freq_bands(x)['Delta'])

def get_mean_theta(x):
    return np.log(get_mean_freq_bands(x)['Theta'])

def get_mean_gamma(x):
    return np.log(get_mean_freq_bands(x)['Gamma'])