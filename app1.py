def divide(a, b):
    return a / b  # нет проверки на 0

def get_user(cursor, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL-инъекция
    return cursor.execute(query)
