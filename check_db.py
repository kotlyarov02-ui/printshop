from sqlalchemy import text

from app.database import engine

with engine.connect() as connection:
    result = connection.execute(
        text("SELECT current_database(), current_user")
    )

    row = result.fetchone()

    print("Результат запроса:", row, flush=True)
    print("База данных:", row[0], flush=True)
    print("Пользователь:", row[1], flush=True)