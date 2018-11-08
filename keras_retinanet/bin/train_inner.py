import os
import sys

# Allow relative imports when being executed as script.
if __name__ == "__main__" and __package__ is None:
    # sys.path: ['~/relPath/keras_retinanet/bin', ...]

    # insert 'keras_retinanet/bin/../..'
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    __package__ = "keras_retinanet.bin"

# relavie imports
from ..utils.clip import clip_maxmin
from .. import layers

# absolute imports
import verify


def main():
    import numpy as np
    data = np.random.normal(loc=0, scale=2, size=(3, 3))
    val = clip_maxmin(data)
    val = layers.sigmoid(val)
    verify.printVer()

if __name__ == '__main__':
    main()
