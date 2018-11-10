1. The home directory of the program
2. PYTHONPATH directories (if set)
3. Standard library directories
4. The contents of any .pth files (if present)
5. The site-packages home of third-party extensions

- Ultimately, the concatenation of these four components becomes `sys.path`, a **mutable**
list of directory name strings.

- The first and third elements of the search path are defined automatically. Because Python searches the concatenation of these components from first to last, though, the second and
fourth elements can be used to extend the path to include your own source code directories.

Home directory (automatic):
> Python **first** looks for the imported file in the home directory

The meaning of this entry depends on how you are running the code.
- When you’re running a program, this entry is the **directory containing your program’s top-level script file**.
- When you’re working interactively, this entry is the directory in which you are
working (i.e., the current working directory).
- imported module inheritate the **same** `Home directory`, i.e. **program’s top-level script file**.

#### one example
project tree:
```bash
work/
├── main.py
├── pkg
    ├── __init__.py
    ├── ml.py
```
<br>

`work/main.py`:
```python
import sys
from pkg.ml import ml_sys

print('module syspath')
print(ml_sys)
print('\n')
print('main syspath')
print(sys.path)
```
<br>

`work/pkg/ml.py`:
```python
import sys

ml_sys = sys.path

if __name__ == '__main__':
    print(ml_sys)
```
<br>

`work/pkg/__init__.py`:
```python
```
####**run**:
1. import module share the same `home directory` i.e.`sys.path[0]` with main program
```bash
$ python work/main.py
```
```bash
module syspath
$:
['~/work', '/home/software/miniconda3/lib/python36.zip', '/home/software/miniconda3/lib/python3.6', '/home/software/miniconda3/lib/python3.6/lib-dynload', '/home/software/miniconda3/lib/python3.6/site-packages']


main syspath
['~/work', '/home/software/miniconda3/lib/python36.zip', '/home/software/miniconda3/lib/python3.6', '/home/software/miniconda3/lib/python3.6/lib-dynload', '/home/software/miniconda3/lib/python3.6/site-packages']
```

2. `home directory` is the directory containing your program’s top-level script file
```bash
$ python work/pkg/ml.py
```
```bash
['~/work/pkg', '/home/software/miniconda3/lib/python36.zip', '/home/software/miniconda3/lib/python3.6', '/home/software/miniconda3/lib/python3.6/lib-dynload', '/home/software/miniconda3/lib/python3.6/site-packages']
```
