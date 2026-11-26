def divide(a, b):
    """Divide a by b.

    Raises:
        ValueError: if b is 0.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def get_user(cursor, user_id):
    query = "SELECT * FROM users WHERE id = %s"
    return cursor.execute(query, (user_id,))
