# Python Variable Annotations :wink:

This repository contains Python scripts focusing on variable annotations, type hints, and type checking.

## Tasks Overview

### 0. Basic annotations - add
- Function: `add(a: float, b: float) -> float`
- Adds two float numbers and returns their sum as a float.

### 1. Basic annotations - concat
- Function: `concat(str1: str, str2: str) -> str`
- Concatenates two strings and returns the resulting string.

### 2. Basic annotations - floor
- Function: `floor(n: float) -> int`
- Takes a float and returns its floor value as an integer.

### 3. Basic annotations - to string
- Function: `to_str(n: float) -> str`
- Takes a float and returns its string representation.

### 4. Define variables
- Variables:
  - `a: int = 1`
  - `pi: float = 3.14`
  - `i_understand_annotations: bool = True`
  - `school: str = "Holberton"`

### 5. Complex types - list of floats
- Function: `sum_list(input_list: List[float]) -> float`
- Takes a list of floats and returns their sum as a float.

### 6. Complex types - mixed list
- Function: `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`
- Takes a list of integers and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple
- Function: `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`
- Takes a string and an int or float, returns a tuple with the string and square of the int/float as a float.

### 8. Complex types - functions
- Function: `make_multiplier(multiplier: float) -> Callable[[float], float]`
- Takes a float and returns a function that multiplies a float by the input.

### 9. Let's duck type an iterable object
- Function: `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]`
- Takes a list of sequences, returns a list of tuples with each sequence and its length.

### 10. Duck typing - first element of a sequence
- Function: `safe_first_element(lst: Sequence[Any]) -> Union[Any, None]`
- Returns the first element of a sequence or None if the sequence is empty.

### 11. More involved type annotations
- Function: `safely_get_value(dct: Mapping, key: Any, default: Optional[T]) -> Union[Any, T]`
- Retrieves a value from a dictionary based on a key, returns the value or a default value.

### 12. Type Checking
- Script: `102-type_checking.py`
- Utilizes mypy for type checking, ensures proper type annotations and handling.

---

## Usage
- Clone the repository:
  ```bash
  git clone https://github.com/your_username/alx-backend-python.git
  ```

- Navigate to the task directory:
  ```bash
  cd alx-backend-python/0x00-python_variable_annotations
  ```

- Run individual scripts or mypy for type checking:
  ```bash
  python 0-main.py
  mypy 102-type_checking.py
  ```

Feel free to explore and use these scripts to understand Python's variable annotations and type hints!
```

This README.md provides an overview of the tasks, their descriptions, and a guide on how to use the scripts within the repository. Adjust the content to match your repository structure and specifics.
