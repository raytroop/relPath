import numpy as np

def clip_maxmin(x, minval=-1.0, maxval=1.0):
    return np.minimum(np.maximum(x, maxval), minval)
