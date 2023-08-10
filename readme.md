# relabs_test

Установка пакетов:
```
pip install -r requirements.txt
cd app
```
Запуск клиента:
```
uvicorn client:app --reload  --port 8000
```
Запуск сервера в другом терминале:
```
uvicorn server:app --reload  --port 8001
```

Адрес страницы (по умолчанию): http://127.0.0.1:8000