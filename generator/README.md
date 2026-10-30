# Generators

Examples of lazy iteration using generator functions.

## Concepts

- A function containing `yield` returns a generator object.
- `next()` resumes execution until the next `yield`.
- Generators produce values on demand instead of building the whole result.
- `firstn_generator` uses less memory than `firstn` for large ranges.
- `countdow` demonstrates generator start and completion messages.
- `fib` yields Fibonacci values below a supplied limit.
- Generators can be consumed by `list`, `sum`, and other iterables.

## Run

```powershell
python .\generator\gen.py
```

Many generator objects are single-use: once consumed, they are exhausted.
