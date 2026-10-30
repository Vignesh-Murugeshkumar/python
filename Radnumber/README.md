# Randomness

Examples of pseudo-random and security-oriented random values.

## Concepts

- [`random_number.py`](./random_number.py) uses `random` for floats, integers,
  sampling, shuffling, distributions, and saved generator state.
- `random.seed(1)` makes the pseudo-random sequence reproducible.
- [`secret.py`](./secret.py) uses `secrets` for values intended for tokens or
  other security-sensitive purposes.
- `secret.py` also demonstrates NumPy arrays, integer generation, seeding, and
  shuffling.

## Run

```powershell
python .\Radnumber\random_number.py
python .\Radnumber\secret.py
```

`secret.py` requires NumPy:

```powershell
python -m pip install numpy
```

Do not use the `random` module for passwords, tokens, or authentication
secrets; use `secrets` instead.
