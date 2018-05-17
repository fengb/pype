# pype

Silly experiment to add Elixir's pipeline operator into Python.

## Example usage

```python
>>> import pype

>>> ([1, 2, 3, 4, 5]
...   | pype.l(filter, lambda x: x%2 == 1)
...   | pype.l(map, lambda x: x**2)
... )
[1, 9, 25]
```
