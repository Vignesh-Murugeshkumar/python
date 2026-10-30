# Decorators

Examples of wrapping functions and classes to add behavior without changing
the decorated function's body.

## Concepts

- [`decorators.py`](./decorators.py) uses `functools.wraps`, a basic decorator,
  and a parameterized decorator that repeats a function call.
- [`classdecor.py`](./classdecor.py) makes a class callable with `__call__` and
  counts function invocations.
- [`nesteddecor.py`](./nesteddecor.py) stacks a debug decorator with a
  start/end decorator.
- `*args` and `**kwargs` allow wrappers to preserve flexible call signatures.

## Run

```powershell
python .\decor\decorators.py
python .\decor\classdecor.py
python .\decor\nesteddecor.py
```

Decorator order matters: stacked decorators are applied from the closest
decorator to the function outward.
