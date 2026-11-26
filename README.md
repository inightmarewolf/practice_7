# Test repo

## triangle_area(a, h)

Пример вычисления площади треугольника по основанию и высоте.

```python
def triangle_area(a: float, h: float) -> float:
    """Calculate triangle area by base and height.

    Raises:
        ValueError: if a <= 0 or h <= 0
    """
    if a <= 0 or h <= 0:
        raise ValueError("Base and height must be positive")
    return a * h / 2


# Example:
# triangle_area(10, 5) -> 25.0
# triangle_area(10, -1) -> ValueError
```
