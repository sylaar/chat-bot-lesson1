# Отправляем уведомления о проверке работ

Чатбот для отправки уведомления о проверки задач на курсе Девман.


## Запуск проекта

1. **Клонировать репозиторий**
```bash
git clone https://github.com/sylaar/chat-bot-lesson1.git
cd chat-bot-lesson1
```
2. **Установить зависимости**

```bash
pip install -r requirements.txt
```
3. **Настроить API-ключи**
Создать файл .env в корне проекта:

```.env
TG_TOKEN='telegram_token'
DEVMAN_TOKEN='devman_token'
```
Запустить скрипт 

```bash
python script.py
```

## Что делает программа
Обращается к https://dvmn.org/api/long_polling/ и сообщает о новой проверке работы, путем отправки сообщения в Телеграм бота.


## Пример запуска
<img width="482" height="118" alt="Снимок экрана — 2026-07-09 в 22 12 27" src="https://github.com/user-attachments/assets/7d1e7c7f-8300-4c79-9ab4-442959c9962c" />