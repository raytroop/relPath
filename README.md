## Allow relative imports when being executed as script

* we can execute script anywhere
```bash
localhost:anywhere$ python path/to/train_inner.py
localhost:anywhere$ python path/to/train_outter.py
```
* [\_\_package\_\_](https://www.python.org/dev/peps/pep-0366/)
> The major proposed change is the introduction of a new module level attribute, `__package__`. **When it is present, relative imports will be based on this attribute rather than the module __name__ attribute.**(`__name__` do not make sense because of `__main__` when executed)
> When the main module is specified by its filename, then the `__package__` attribute will be set to None. To allow relative imports when the module is executed directly, boilerplate similar to the following would be needed before the first relative import statement:
```python
if __name__ == "__main__" and __package__ is None:
    __package__ = "expected.package.name"
```
> **Note that this boilerplate is sufficient only if the top level package is already accessible via `sys.path`.** Additional code that manipulates sys.path would be needed in order for direct execution to work without the top level package already being importable.

**credits:**
[fizyr/keras-retinanet](https://github.com/fizyr/keras-retinanet/blob/a0d99cbb44b1eaa909c34c88833d501a83322767/keras_retinanet/bin/train.py#L28-L32)