# Threads and Processes

A direct comparison between thread-based and process-based execution.

## Files

- [`multi.py`](./multi.py) starts ten threads, each calculating a square.
- [`theradandmultiprocess.py`](./theradandmultiprocess.py) starts one process
  per available CPU (or one if CPU count is unavailable).

Both examples start workers, wait with `join()`, and then print a completion
message.

## Run

```powershell
python .\threadAndMultiproce\multi.py
python .\threadAndMultiproce\theradandmultiprocess.py
```

Threads share the process memory and are lightweight; processes have separate
memory and can use multiple CPU cores for CPU-bound work.
