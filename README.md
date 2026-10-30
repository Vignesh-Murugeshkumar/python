# Python Concepts

Small, runnable examples for learning core Python and standard-library concepts.

## Topics

| Topic | What it covers |
| --- | --- |
| [Object-oriented programming](./oop/README.md) | Classes, inheritance, class methods, static methods, and CSV loading |
| [Logging](./logg/README.md) | Log levels, formatters, stream handlers, and file handlers |
| [Multiprocessing](./multiprocessing/README.md) | Processes, shared values and arrays, locks, queues, and pools |
| [Decorators](./decor/README.md) | Function, parameterized, class-based, and nested decorators |
| [Randomness](./Radnumber/README.md) | Pseudo-random values, reproducible seeds, secure randomness, and NumPy |
| [Threading](./threading/README.md) | Threads, locks, queues, worker threads, and task completion |
| [Threads and processes](./threadAndMultiproce/README.md) | Side-by-side thread and process execution |
| [Function arguments](./funarg/README.md) | Positional, keyword, unpacked, and variadic arguments |
| [Generators](./generator/README.md) | `yield`, lazy iteration, generator memory usage, and Fibonacci |
| [Exception handling](./exitingcodetopython/README.md) | `try`, `except`, `else`, `finally`, and exception messages |

## Standalone examples

- [`collector.py`](./collector.py) demonstrates `collections` containers.
- [`iter.py`](./iter.py) demonstrates `itertools` combinations and grouping.
- [`lamb.py`](./lamb.py) demonstrates lambdas, `map`, `filter`, and `reduce`.
- [`expectio.py`](./expectio.py) demonstrates exception handling.
- [`fuctions.py`](./fuctions.py) demonstrates basic function calls.

## Running an example

From the repository root, run any script with Python:

```powershell
python .\generator\gen.py
python .\oop\main.py
```

The examples target modern Python 3. Some scripts intentionally print intermediate
values to make execution order and state changes visible.