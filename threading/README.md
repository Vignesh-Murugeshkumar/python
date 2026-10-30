# Threading

Examples of concurrent work with Python threads.

## Concepts

- [`theread.py`](./theread.py) protects a shared counter with `Lock`.
- [`que.py`](./que.py) implements a worker-thread pattern with `Queue`.
- `Queue.task_done()` and `Queue.join()` coordinate completion.
- `None` is used as a sentinel telling each worker to stop.
- Thread `join()` waits for worker completion before the main thread exits.

## Run

```powershell
python .\threading\theread.py
python .\threading\que.py
```

Threads are useful for overlapping I/O-bound work. Shared mutable state still
needs synchronization.
