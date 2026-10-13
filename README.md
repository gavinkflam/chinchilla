# Chinchilla

My solutions to algorithm exercises.

## Setup

1. Install Python 3 using [asdf](https://asdf-vm.com/guide/getting-started.html), or using your favorite package manager / version management system.
2. Install virtualenv, e.g. `pip install virtualenv`.
3. Create virtualenv, e.g. `python -m venv .venv`.
4. Activate virtualenv, e.g. `source .venv/bin/activiate`.
5. Install dependencies.
    - `pip install -r requirements.txt`
    - `pip install -r requirements-dev.txt`.

## Development

### Tests

Run all tests.

`python -m unittest`

Run a single test.

`python -m unittest tests.test_dpv_ch6_ex1`

### Formatting

Use [Black](https://github.com/psf/black) to auto-format code.

`black $(git ls-files '*.py')`

### Linting

`pylint $(git ls-files '*.py')`

## License

MIT
