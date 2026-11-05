import os
import pytest
from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://"
    "postgres:password"
    "@localhost:5432/sql_praktika"
)


@pytest.fixture
def db_engine():
    engine = create_engine(DATABASE_URL)
    return engine


def test_add_student(db_engine):
    """Тест на ДОБАВЛЕНИЕ студента."""
    with db_engine.connect() as connection:
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


def test_update_student(db_engine):
    """Тест на ИЗМЕНЕНИЕ данных студента."""
    with db_engine.connect() as connection:
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


def test_delete_student(db_engine):
    """Тест на УДАЛЕНИЕ студента."""
    with db_engine.connect() as connection:
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
