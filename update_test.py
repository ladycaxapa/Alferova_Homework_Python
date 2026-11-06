import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://"
    "postgres:password"
    "@localhost:5432/sql_praktika"
)


def test_update_student():
    """Тест на ИЗМЕНЕНИЕ данных студента."""
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        # Подготовка чистых данных для теста
        connection.execute(
            text("DELETE FROM student WHERE user_id = 9999")
        )
        connection.execute(
            text(
                "INSERT INTO student (user_id, level) "
                "VALUES (9999, 'Junior')"
            )
        )

        # Изменяем уровень
        connection.execute(
            text(
                "UPDATE student SET level = 'Middle' "
                "WHERE user_id = 9999"
            )
        )

        # Проверяем изменения
        res = connection.execute(
            text(
                "SELECT level FROM student "
                "WHERE user_id = 9999"
            )
        ).fetchone()

        assert res is not None
        assert res[0] == "Middle"

        # Чистим за собой базу данных
        connection.execute(
            text("DELETE FROM student WHERE user_id = 9999")
        )
