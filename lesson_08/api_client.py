import requests
from config import BASE_URL, HEADERS


class YougileProjectClient:
    """Класс-клиент для взаимодействия с API проектов YouGile."""

    def __init__(self):
        self.base_url = f"{BASE_URL}/projects"
        self.headers = HEADERS

    def create_project(self, title: str, users: dict = None):
        """[POST] /api-v2/projects — Создание нового проекта"""
        payload = {}
        if title is not None:
            payload["title"] = title
        if users:
            payload["users"] = users
        return requests.post(self.base_url, json=payload, headers=self.headers)

    def get_project(self, project_id: str):
        """[GET] /api-v2/projects/{id} — Получение информации"""
        url = f"{self.base_url}/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, new_title: str):
        """[PUT] /api-v2/projects/{id} — Обновление параметров"""
        url = f"{self.base_url}/{project_id}"
        payload = {}
        if new_title is not None:
            payload["title"] = new_title
        return requests.put(url, json=payload, headers=self.headers)

    def delete_project(self, project_id: str):
        """[DELETE] /api-v2/projects/{id} — Удаление проекта"""
        url = f"{self.base_url}/{project_id}"
        return requests.delete(url, headers=self.headers)
