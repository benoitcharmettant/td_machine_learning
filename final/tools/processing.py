import time
import datetime

from pandas import DataFrame, read_csv, concat

from numpy import zeros

def extract_features(func_class, data, sample=None, col=["eeg_1","eeg_2","eeg_3","eeg_4","eeg_5","eeg_6","eeg_7"], verbose_end='\r'):
    # 
    n = len(data['eeg_1'])

    spl = sample
    
    if spl is None:
        spl = [i for i in range(n)]
        
    n_sample = len(spl)
    
    features_names = [n for f in func_class for n in f.f_names]
    n_features = len(features_names)
    columns = [f"{col_name}_{f_name}" for col_name in col for f_name in features_names]
    n_columns = len(columns)
        
    res = DataFrame(columns=columns)
    c=1
    for index in spl:
        t1 = time.time()
        c+=1
        
        feat = zeros(n_columns)
        
        for j, name in enumerate(col):
            i = 0
            for fc in func_class:
                feat[n_features*j+i:n_features*j+i+fc.n_outs] = fc.f(data[f"{name}"][index])
                i+=fc.n_outs
                
        feat = dict(zip(columns, feat))
        res = res.append(feat, ignore_index=True)
        
        t2 = time.time()
        print(f">>> {c} / {n_sample} <<< (Remains : {str(datetime.timedelta(seconds=(t2 - t1)*(n_sample-c)))})", end=verbose_end)
    return res

def extract_all_features(func_class, data, save, col=["eeg_1","eeg_2","eeg_3","eeg_4","eeg_5","eeg_6","eeg_7"], verbose_end='\r'):
    spl = [i for i in range(len(data['eeg_1']))]
    features = extract_features(func_class, data, sample=spl, col=col, verbose_end=verbose_end)
    features['abs_index'] = spl
    features.to_csv(save)
    
def load_features(path):
    features = read_csv(path)
    features = features.drop(['Unnamed: 0'], axis=1)
    return features

def merge_features(ls_features):
    for i in range(1, len(ls_features)):
        ls_features[i] = ls_features[i].drop(['abs_index'], axis=1)
        
    return concat(ls_features, axis=1)