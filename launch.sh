#!/bin/bash
echo 'Запускаем сервер streamlit'
cd ml_web_app/
source ../python_venv/streamlit/bin/activate
streamlit run ml_web_app.py