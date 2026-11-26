# Test repo

## divide(a, b)

Пример безопасного деления с проверкой деления на ноль.

```python
def divide(a: float, b: float) -> float:
    """Divide a by b.

    Raises:
        ValueError: if b == 0
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# Example:
# divide(10, 2) -> 5.0
# divide(10, 0) -> ValueError
```
