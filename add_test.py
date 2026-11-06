import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://"
    "postgres:password"
    "@localhost:5432/sql_praktika"
)


def test_add_student():
    """Тест на ДОБАВЛЕНИЕ студента."""
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        # Зачищаем старые тестовые данные
        connection.execute(
            text("DELETE FROM student WHERE user_id = 9999")
        )

        # Добавляем студента
        connection.execute(
            text(
                "INSERT INTO student (user_id, level) "
                "VALUES (9999, 'Junior')"
            )
        )

        # Проверяем, что студент появился в БД
        res = connection.execute(
            text(
                "SELECT level FROM student "
                "WHERE user_id = 9999"
            )
        ).fetchone()

        assert res is not None
        assert res[0] == "Junior"

        # Удаляем за собой созданные данные
        connection.execute(
            text("DELETE FROM student WHERE user_id = 9999")
        )
