# Logging

Demonstrates Python's `logging` module with multiple handlers.

## Concepts

- A logger emits messages at levels such as `INFO`, `WARNING`, and `ERROR`.
- A formatter controls timestamps and message layout.
- `StreamHandler` writes selected messages to the console.
- `FileHandler` writes selected messages to `app.log`.
- Handler levels can differ: this example displays warnings but records errors
  in the file handler.
- `helper.py` shows module-level logger configuration; `log.py` imports it.

## Run

Run from this directory so the relative `app.log` path is predictable:

```powershell
cd .\logg
python .\log.py
cd ..
```

The script may create or update `app.log` in the current working directory.
