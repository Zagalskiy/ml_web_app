#!/bin/bash
echo 'Переходим в каталог репозитория'
cd ml_web_app/
echo 'Чтение библиотек в requirements'
cat requirements.txt
echo 'Устанавливаем Python 3 в каталоге /ml_web_app'
sudo apt install python-is-python3
echo 'Создаем каталог для виртуальных окружений'
mkdir ../python_venv
echo 'Создаем виртуальное окружение'
python -m venv /home/gigabyte727/python_venv/streamlit
echo 'Запуск виртуального окружения'
source /home/gigabyte727/python_venv/streamlit/bin/activate
echo 'Установка библиотек из requirements'
sudo apt install pip
pip install -r requirements.txt
echo 'Запускаем сервер streamlit'
streamlit run ml_web_app.py