# Asynchronous Programming in Python :smile:

This repository contains Python code that demonstrates the concepts and implementations of asynchronous programming using coroutines and tasks.

## Files

### 0-basic_async_syntax.py

Contains an asynchronous coroutine `wait_random` that waits for a random delay between 0 and a specified maximum delay (default is 10 seconds) and returns the delay.

### 1-concurrent_coroutines.py

Implements an async routine `wait_n` that spawns `wait_random` coroutine `n` times with a specified maximum delay. Returns a list of delays in ascending order.

### 2-measure_runtime.py

Imports `wait_n` from the previous file and measures the total execution time for `wait_n(n, max_delay)` with given integers `n` and `max_delay`. Returns the average execution time per coroutine.

### 3-tasks.py

Defines a function `task_wait_random` that takes an integer `max_delay` and returns an asyncio.Task for `wait_random`.

### 4-tasks.py

Similar to `wait_n` but uses `task_wait_random` to create asyncio tasks. Defines `task_wait_n` that spawns tasks and returns a list of delays.

## Instructions

To test each file's functionality, run the corresponding `main.py` files:

- `0-main.py`: Tests the `wait_random` coroutine.
- `1-main.py`: Tests the `wait_n` coroutine for concurrent execution.
- `2-main.py`: Measures the runtime for executing `wait_n`.
- `3-main.py`: Tests the `task_wait_random` function.
- `4-main.py`: Tests the `task_wait_n` function.

## How to Run

1. Clone this repository:

    ```
    git clone https://github.com/your_username/alx-backend-python.git
    ```

2. Navigate to the directory of the task you want to test:

    ```
    cd 0x01-python_async_function/
    ```

3. Run the respective `main.py` file:

    ```
    ./0-main.py
    ```

Feel free to explore each file for more detailed implementations and further understanding of asynchronous programming in Python.
```
