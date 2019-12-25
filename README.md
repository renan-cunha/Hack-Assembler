# Hack Assembler

This is an Assembler of the Hack Machine Language written in Python3.
This is the [6th project](https://www.nand2tetris.org/project06) of the Nand2Tetris Book/Course

### Usage

```bash
python3 main.py assembly_file binary_file
```

#### Example

```
python3 main.py tests/Pong.asm /tmp/Pong.hack
```

## Running the Tests

```bash
pytest-3 tests/
```

#### Show Coverage

```bash
pytest-3 --cov=src/ tests/
```
