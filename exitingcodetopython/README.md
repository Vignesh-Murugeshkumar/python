# Exception Handling

Demonstrates the structure of Python's `try` statement.

## Concepts

- `try` contains code that may raise an exception.
- `except ZeroDivisionError` handles a specific failure.
- `as e` captures the exception object so its message can be printed.
- `else` runs only when the `try` block succeeds.
- `finally` runs whether an exception occurred or not.

## Run

```powershell
python .\exitingcodetopython\test.py
```

The example intentionally triggers a division-by-zero error, then continues
through the remaining handlers to show their execution behavior.
