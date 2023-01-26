#!/bin/bash
echo 'Запускаем сервер streamlit'
cd ml_web_app/
source /home/gigabyte727/python_venv/streamlit/bin/activate (При корректном запуске перед пользователем появится надпись (streamlit) )
streamlit run ml_web_app.py