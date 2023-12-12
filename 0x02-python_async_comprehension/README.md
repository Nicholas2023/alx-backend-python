# Python Async Comprehension Tasks :smile:

This repository contains Python code that demonstrates the usage of asynchronous generators and comprehensions. The tasks involve generating random numbers asynchronously and collecting them using async comprehensions.

## Tasks Overview

### Task 0: Async Generator

File: `0-async_generator.py`

- Implements an asynchronous generator `async_generator` that yields random numbers between 0 and 10.
- It asynchronously waits for 1 second in each iteration and yields a random number.

### Task 1: Async Comprehensions

File: `1-async_comprehension.py`

- Imports `async_generator` from Task 0 and uses an async comprehension to collect 10 random numbers.
- The `async_comprehension` coroutine utilizes async comprehensions to gather the random numbers generated asynchronously.

### Task 2: Runtime Measurement for Parallel Comprehensions

File: `2-measure_runtime.py`

- Imports `async_comprehension` from Task 1 and measures the total runtime for running `async_comprehension()` four times in parallel.
- Utilizes `asyncio.gather()` to execute the comprehensions concurrently and measures the total time taken.

## Instructions

1. Clone the repository: `git clone <repository_url>`
2. Install Python (if not already installed).
3. Navigate to the directory `0x02-python_async_comprehension`.
4. Run each Python file using `python <filename>` or `python3 <filename>`.

### Running the Scripts

- **Task 0**: Run `0-async_generator.py` to see the async generator in action.
- **Task 1**: Execute `1-async_comprehension.py` to collect 10 random numbers using async comprehensions.
- **Task 2**: Run `2-measure_runtime.py` to measure the total runtime for running async comprehensions in parallel.

Ensure you have the necessary permissions and dependencies installed before running the scripts.

## Dependencies

- Python 3.x
- asyncio library

## Example Usage

```bash
# Execute Task 0 - Async Generator
python 0-async_generator.py

# Execute Task 1 - Async Comprehensions
python 1-async_comprehension.py

# Execute Task 2 - Runtime Measurement for Parallel Comprehensions
python 2-measure_runtime.py
```
