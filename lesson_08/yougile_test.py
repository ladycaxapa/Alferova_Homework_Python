import uuid
import pytest
import config
from api_client import YougileProjectClient

# Если токен не передан в систему, pytest пропустит тесты
pytestmark = pytest.mark.skipif(
    not config.TOKEN,
    reason="Тесты пропущены: Не задана переменная окружения YOUGILE_TOKEN"
)


@pytest.fixture(scope="function")
def api_client():
    """Фикстура для инициализации API-клиента перед каждым тестом."""
    return YougileProjectClient()


# ==========================================
# ПОЗИТИВНЫЕ ТЕСТЫ (Positive Tests)
# ==========================================

def test_positive_create_project(api_client):
    """Позитивный тест [POST] — Создание проекта с валидным названием."""
    unique_title = f"Autotest Project {uuid.uuid4().hex[:6]}"

    response = api_client.create_project(title=unique_title)
    msg = f"Ожидался статус 201. Ответ: {response.text}"
    assert response.status_code == 201, msg

    data = response.json()
    assert "id" in data, "В ответе отсутствует id созданного проекта"

    # Очистка данных после теста
    api_client.delete_project(data["id"])


def test_positive_get_project(api_client):
    """Позитивный тест [GET] — Получение проекта и проверка данных."""
    unique_title = f"Autotest Get {uuid.uuid4().hex[:6]}"

    create_res = api_client.create_project(title=unique_title)
    assert create_res.status_code == 201, "Не удалось создать проект для GET"
    project_id = create_res.json()["id"]

    try:
        response = api_client.get_project(project_id)
        assert response.status_code == 200
        assert response.json()["title"] == unique_title
    finally:
        api_client.delete_project(project_id)


def test_positive_update_project(api_client):
    """Позитивный тест [PUT] — Обновление названия и проверка данных."""
    unique_title = f"Autotest Base {uuid.uuid4().hex[:6]}"
    updated_title = f"Autotest Update {uuid.uuid4().hex[:6]}"

    create_res = api_client.create_project(title=unique_title)
    assert create_res.status_code == 201, "Не удалось создать проект для PUT"
    project_id = create_res.json()["id"]

    try:
        response = api_client.update_project(project_id,
                                             new_title=updated_title)
        assert response.status_code == 200

        get_res = api_client.get_project(project_id)
        assert get_res.json()["title"] == updated_title
    finally:
        api_client.delete_project(project_id)


# ==========================================
# НЕГАТИВНЫЕ ТЕСТЫ (Negative Tests)
# ==========================================

def test_negative_create_project_missing_title(api_client):
    """Негативный тест [POST] — Создание без обязательного поля title."""
    response = api_client.create_project(title=None)
    assert response.status_code == 400

    error_data = response.json()
    assert "message" in error_data or "error" in error_data
    assert "title" in str(error_data).lower()


def test_negative_get_project_not_found(api_client):
    """Негативный тест [GET] — Запрос проекта по несуществующему UUID."""
    fake_id = str(uuid.uuid4())
    response = api_client.get_project(fake_id)
    assert response.status_code == 404

    error_data = response.json()
    assert "message" in error_data
    msg_lower = error_data["message"].lower()
    assert "not found" in msg_lower or "не найден" in msg_lower


def test_negative_update_project_not_found(api_client):
    """Негативный тест [PUT] — Обновление проекта с несуществующим UUID."""
    fake_id = str(uuid.uuid4())
    response = api_client.update_project(fake_id, new_title="Ghost Project")
    assert response.status_code == 404

    error_data = response.json()
    assert "message" in error_data
    msg_lower = error_data["message"].lower()
    assert "not found" in msg_lower or "не найден" in msg_lower
