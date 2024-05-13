# Проект Торговой Сети

## Описание

Проект Торговой Сети - это RESTful API, предназначенный для управления участниками торговой сети, включая заводы, розничные сети и индивидуальных предпринимателей. Система позволяет управлять узлами сети, их продуктами и контактной информацией, а также контролировать иерархические связи между различными уровнями сети.

## Технологии

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+
- PostgreSQL

## Установка

### Клонирование репозитория

```bash
git clone https://your-repository-url.git
cd your-project-directory
```
Настройка виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
```
Установка зависимостей
```bash
pip install -r requirements.txt
```
### Настройка базы данных
Измените настройки в settings.py для подключения к вашей PostgreSQL базе данных.

Применение миграций
```bash
python manage.py migrate
```
Запуск проекта
```bash
python manage.py runserver
```

Использование
Доступ к API осуществляется через следующие эндпоинты:

POST /api/retailers/create-retailer/ - создание нового участника сети.
GET /api/retailers/{id}/ - получение информации о участнике сети.
PUT /api/retailers/{id}/ - обновление информации участника сети.
DELETE /api/retailers/{id}/ - удаление участника сети.