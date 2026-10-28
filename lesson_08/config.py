import os

# Базовый URL для запросов к API YouGile
BASE_URL = "https://yougile.com"

# Код ищет токен в переменных окружения системы.
# Если его нет — будет пустая строка.
TOKEN = os.getenv("YOUGILE_TOKEN", "")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
