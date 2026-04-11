---
name: testing
description: Testing conventions using pytest. Use when writing tests, creating fixtures, or running test suites.
---

# Testing Standards

## Framework
- Use pytest for all tests
- Target 80%+ code coverage

## File Organization
- Tests in `tests/` directory mirroring `src/` structure
- Test files: `test_<module>.py` or `<module>_test.py`
- Test functions: `test_<description>`

## Fixtures
- Use fixtures for reusable test data
- Prefer `scope="function"` unless shared state is needed
- Use `conftest.py` for shared fixtures

Example:
```python
import pytest

@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return User(name="Test User", email="test@example.com")

def test_user_creation(sample_user):
    assert sample_user.name == "Test User"
    assert sample_user.email == "test@example.com"
```

## Parametrization
- Use `@pytest.mark.parametrize` for testing multiple inputs
- Keep parameter names descriptive

Example:
```python
@pytest.mark.parametrize("input_val,expected", [
    (1, 2),
    (2, 4),
    (0, 0),
])
def test_double(input_val, expected):
    assert double(input_val) == expected
```

## Assertions
- Use plain `assert` statements
- Write clear assertion messages for complex checks
- Test one concept per test function

## Mocking
- Use `pytest-mock` or `unittest.mock`
- Mock external dependencies (APIs, databases)
- Avoid mocking the code under test

## Commands
- Run tests: `pytest`
- With coverage: `pytest --cov`
- Verbose: `pytest -v`
- Single file: `pytest tests/test_specific.py`
- Single test: `pytest tests/test_specific.py::test_name`
