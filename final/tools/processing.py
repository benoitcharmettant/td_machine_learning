import time
import datetime

from pandas import DataFrame, read_csv, concat

def extract_features(func, data, sample=None, col=["eeg_1","eeg_2","eeg_3","eeg_4","eeg_5","eeg_6","eeg_7"]):
    n = len(data['eeg_1'])

    spl = sample
    
    if spl is None:
        spl = [i for i in range(n)]
        
    n_sample = len(spl)
        
    res = DataFrame(columns=[f"{name}_{f.__name__}" for name in col for f in func])
    c=1
    for index in spl:
        t1 = time.time()
        print(f">>> {c} / {n_sample} <<<", end="\r")
        c+=1
        feat = [0 for i in range(len(func)*len(col))]
        
        for i, f in enumerate(func):
            for j, name in enumerate(col):
                feat[len(func)*j+i] = f(data[f"{name}"][index])
                
        feat = dict(zip(res.columns, feat))
        res = res.append(feat, ignore_index=True)
        
        t2 = time.time()
        print(f">>> {c} / {n_sample} <<< (Remains : {str(datetime.timedelta(seconds=(t2 - t1)*(n_sample-c)))})", end="\r")
    return res

def extract_all_features(func, data, save, col=["eeg_1","eeg_2","eeg_3","eeg_4","eeg_5","eeg_6","eeg_7"]):
    spl = [i for i in range(len(data['eeg_1']))]
    features = extract_features(func, data, sample=spl, col=col)
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