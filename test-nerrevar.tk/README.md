Необходимо установить необходимые зависимости и запустить 2 сервера:

serve -s build

и в папке python:

gunicorn test_app:app