---
name: code-style
description: Python code style and formatting standards using Ruff. Use when writing or reviewing Python code.
---

# Python Code Style

## Formatting
- Use Ruff for formatting (`ruff format .`)
- Indentation: 4 spaces
- Max line length: 120 characters
- Use trailing commas in multi-line collections

## Naming Conventions
- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`
- Module files: `snake_case.py`

## Type Hints
- Required for all function parameters and return types
- Use `Optional[T]` or `T | None` for nullable types
- Use `list[T]`, `dict[K, V]` (lowercase) for Python 3.10+

## Docstrings
- Use Google-style docstrings
- Required for all public functions, classes, and modules
- Include Args, Returns, and Raises sections

Example:
```python
def calculate_total(items: list[Item], discount: float = 0.0) -> float:
    """Calculate the total price of items with optional discount.

    Args:
        items: List of items to calculate total for.
        discount: Discount percentage to apply (0.0 to 1.0).

    Returns:
        The total price after discount.

    Raises:
        ValueError: If discount is not between 0 and 1.
    """
```

## Imports
- Sort with Ruff (replaces isort)
- Group: stdlib, third-party, local
- Use absolute imports for clarity
- Avoid wildcard imports (`from x import *`)

## Commands
- Format: `ruff format .`
- Lint: `ruff check .`
- Fix: `ruff check --fix .`
