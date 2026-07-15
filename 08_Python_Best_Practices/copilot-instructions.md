---
applyTo: 08_Python_Best_Practices/**/*.py
description: Python Best Practices guide for code generation and suggestions
---

# Python Best Practices for Copilot

This instruction set enforces Python best practices across all code in the `08_Python_Best_Practices` folder.

## 1. PEP 8 Compliance

### Code Style Rules
- Use **4 spaces** for indentation (never tabs)
- Maximum line length: **79 characters** (PEP 8 standard)
- Use **snake_case** for function and variable names
- Use **PascalCase** for class names
- Add **blank lines** between top-level functions/classes (2 lines)
- Add **single blank line** between methods in a class
- Avoid trailing whitespace

### Spacing Guidelines
```python
# ✅ CORRECT
def calculate_area(length, width):
    result = length * width
    return result

# ❌ AVOID
def calculateArea(length,width):
    result=length*width
    return result
```

---

## 2. Type Hints

### Requirements
- **ALL functions** must include type hints for parameters and return types
- Use `from typing import` for complex types (`List`, `Dict`, `Optional`, `Union`, etc.)
- Format: `def function_name(param: type) -> return_type:`

### Type Hint Patterns
```python
# ✅ CORRECT - Basic types
def add(a: int, b: int) -> int:
    return a + b

# ✅ CORRECT - Optional types
def find_user(user_id: int) -> Optional[str]:
    return name or None

# ✅ CORRECT - Multiple parameters with hints
def calculate_total(
    maths: int,
    science: int,
    english: int
) -> int:
    return maths + science + english

# ❌ AVOID - No type hints
def add(a, b):
    return a + b
```

---

## 3. Exception Handling

### Best Practices
- **Always catch specific exceptions**, never bare `except:`
- Use separate `except` blocks for different exception types
- Include a **`finally` block** for cleanup when appropriate
- Never suppress exceptions without logging/handling
- Provide meaningful error messages

### Exception Handling Pattern
```python
# ✅ CORRECT
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program Finished")

# ❌ AVOID - Bare except or generic message
try:
    result = 100 / number
except:
    print("Error occurred")
```

---

## 4. Docstrings

### Docstring Requirements
- **Every function and class** must have a docstring
- Use **triple double quotes** (`"""..."""`)
- One-line functions: keep docstring on one line
- Multi-line: description on first line, blank line, then details

### Google Style (Preferred)
```python
# ✅ CORRECT - Google style
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Product of a and b.
    """
    return a * b
```

### NumPy Style (Alternative)
```python
def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        Dividend.
    b : float
        Divisor.

    Returns
    -------
    float
        Quotient of division.
    """
    return a / b
```

### Classes
```python
class Calculator:
    """
    A simple calculator for mathematical operations.
    
    Attributes:
        value (float): Current calculator value.
    """
```

---

## 5. Unit Testing

### Testing Framework
- Use **`unittest`** framework (built-in, no external dependencies)
- Test file naming: `test_*.py` or `*_test.py`
- Test class naming: `Test*` (e.g., `TestCalculator`)
- Test method naming: `test_*` (e.g., `test_add_positive_numbers`)

### Test Structure
```python
# ✅ CORRECT
import unittest

def add(a: int, b: int) -> int:
    return a + b

class TestMathOperations(unittest.TestCase):
    """Test cases for math operations."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-10, -5), -15)

if __name__ == "__main__":
    unittest.main()
```

### Assertion Methods
- `assertEqual(a, b)` - Check equality
- `assertNotEqual(a, b)` - Check inequality
- `assertTrue(x)` - Assert x is True
- `assertFalse(x)` - Assert x is False
- `assertRaises(Exception)` - Assert exception is raised

---

## 6. Code Organization

### Module Structure
```
module.py
├── Imports
├── Constants (ALL_CAPS)
├── Helper functions
├── Main classes
├── Main functions
└── if __name__ == "__main__":
```

### Imports Order
1. Standard library imports
2. Third-party imports
3. Local application imports
(Each group separated by blank line)

---

## 7. Common Patterns to Follow

### ✅ Example: Complete Best Practices
```python
"""
Calculator module for basic mathematical operations.

This module demonstrates Python best practices including type hints,
exception handling, and proper documentation.
"""

from typing import Union


def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of the rectangle.
        width (float): Width of the rectangle.

    Returns:
        float: Area of the rectangle.

    Raises:
        ValueError: If dimensions are not positive.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive.")
    return length * width


def safe_divide(a: float, b: float) -> Union[float, None]:
    """
    Safely divide two numbers.

    Args:
        a (float): Dividend.
        b (float): Divisor.

    Returns:
        Union[float, None]: Result of division or None if divisor is zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None


if __name__ == "__main__":
    area = calculate_area(10, 5)
    print(f"Area: {area}")
```

---

## Checklist for Code Review

Before committing code in this folder, verify:
- [ ] All functions have type hints
- [ ] All functions/classes have docstrings (Google or NumPy style)
- [ ] PEP 8 compliance (4-space indents, snake_case, proper spacing)
- [ ] Specific exception handling (no bare `except:`)
- [ ] Unit tests written for new functions
- [ ] Code follows the organizational structure
- [ ] No lines exceed 79 characters (with reasonable exceptions)

---

## Quick Reference

| Aspect | Standard |
|--------|----------|
| **Indentation** | 4 spaces |
| **Line Length** | 79 characters |
| **Naming** | snake_case for functions/vars, PascalCase for classes |
| **Type Hints** | Required on all functions |
| **Docstrings** | Google style (preferred) or NumPy style |
| **Exception Handling** | Specific exceptions only, always catch properly |
| **Testing Framework** | unittest |
| **Blank Lines** | 2 between top-level definitions, 1 between methods |
