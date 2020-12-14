import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from tools.processing import *

from pandas import DataFrame

def boxplot_feature(name, data, meta, spl, ax, func):
    eegs = data[name]
    prop = [0 for i in range(len(spl))]

    for j, i in enumerate(spl):
        prop[j] = func(eegs[i])
        
    res = DataFrame(columns=['feature', 'sleep_stage'])
    res['feature'] = prop
    res['sleep_stage'] = meta['label'].values[spl].astype(np.int)
    sns.boxplot(y='feature', x='sleep_stage', data=res, ax=ax)
    
def compare_feature(func, data, meta, sample=None, col=["eeg_1","eeg_2","eeg_3","eeg_4","eeg_5","eeg_6","eeg_7"]): 
    n = len(data['eeg_1'])
    n_samples = len(sample)
    
    spl = sample
    
    if spl is None:
        spl = [i for i in range(n)]

    fig, axes = plt.subplots(1, len(col), sharey=True)
    plt.rcParams['figure.figsize'] = [20, 5]

    for i, name in enumerate(col):
        boxplot_feature(name, data, meta, spl, ax=axes[i-1], func=func)
        axes[i-1].set_title(name)
        
        if not i == 0:
            axes[i-1].get_yaxis().set_visible(False)
    plt.show()
    
def plot_eeg(abs_index, raw_data, meta_data):
    plt.rcParams['figure.figsize'] = [20, 5]
    i = abs_index
    fig= plt.figure()
    fig.suptitle(f"EEG - Absolute index {i} - Sleep Stage = {meta_data['label'][i]}")
    for j in range(7):
        name = f"eeg_{j+1}"
        ax = fig.add_subplot(7, 1, j+1)
        for loc, spines in ax.spines.items():
            if not loc == 'left':
                spines.set_color('none')
        ax.plot(raw_data[name][i])
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.yaxis.set_ticks_position('left')
        
    ax.xaxis.set_ticks_position('bottom')
    plt.show()