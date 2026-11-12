import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://"
    "postgres:password"
    "@localhost:5432/sql_praktika"
)


def test_delete_student():
    """Тест на УДАЛЕНИЕ студента."""
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        # Подготовка: добавляем студента
        connection.execute(
            text("DELETE FROM student WHERE user_id = 9999")
        )
        connection.execute(
            text(
                "INSERT INTO student (user_id, level) "
                "VALUES (9999, 'Junior')"
            )
        )

        # Удаляем созданного студента
        connection.execute(
            text("DELETE FROM student WHERE user_id = 9999")
        )

        # Проверяем, что его больше нет в БД
        res = connection.execute(
            text(
                "SELECT * FROM student "
                "WHERE user_id = 9999"
            )
        ).fetchone()

        assert res is None
