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
