```bash
localhost:work$ python scripts/shuffle_patients.py
```
<br>

`work/scripts/shuffle_patients.py`
```python
# insert `scripts` into `sys.path`
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
# print(sys.path)
from rsna.datasets.rsna_train_dataset import class_names
```

#### caution
Dont mix python `module search path` with `filepath to read` of **pd.read_csv / to_csv**.
- `filepath to read` is always relative the `current working directory` where you execuate script i.e. `os.getcwd()`.
In this way, `pd.read_csv` read `'./RSNA/stage_2_detailed_class_info.csv'` and output to `'./resources/stage_2_patients_shuffled.csv'`. But `os.chdir`
can change the current working directory to the given path.
- `module search path` has nothing to with where script is executated, instead, where script is in.

#### reference
- [pfnet-research/pfneumonia](https://github.com/pfnet-research/pfneumonia)
