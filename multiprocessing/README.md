# Multiprocessing

Examples of parallel work using Python's `multiprocessing` module.

## Concepts

- `Process` starts independent worker processes.
- `Value` and `Array` provide shared memory between processes.
- `Lock` protects updates to shared state from races.
- `Queue` can be used to pass results between processes.
- `Pool.map` distributes work across a fixed pool of workers.
- `current_process().name` identifies the process producing output.

## Files

- [`multiproce.py`](./multiproce.py): synchronized increments of a shared `Value`.
- [`array.py`](./array.py): synchronized updates to a shared `Array`.
- [`poool.py`](./poool.py): maps square-number work through a process pool.
- [`q.py`](./q.py): additional queue-based process example.

## Run

```powershell
python .\multiprocessing\multiproce.py
python .\multiprocessing\array.py
python .\multiprocessing\poool.py
python .\multiprocessing\q.py
```

The `if __name__ == "__main__":` guard is required when starting processes,
especially on Windows.
