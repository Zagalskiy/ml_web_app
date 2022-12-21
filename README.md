[![Tests](https://github.com/Zagalskiy/ml_web_app/actions/workflows/python-app.yml/badge.svg)](https://github.com/Zagalskiy/ml_web_app/actions/workflows/python-app.yml)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nyc-uber.streamlit.app/)

# Web-приложение на основе библиотеки Streamlit: райдшеринг Uber в Нью-Йорке

Демонстрационное Web-приложение [Streamlit](https://streamlit.io) [написанное на чистом Питоне](https://github.com/Zagalskiy/ml_web_app/blob/main/ml_web_app.py) для интерактивной визуализации подачи машин райдшеринга Uber в Нью-Йорке и в его крупных аэропортах с течением времени.

Используются библиотеки:
- Altair
- Numpy
- Pandas
- Pydeck
- Streamlit

Тестирует GitHub Actions и проверяет работоспособность Web-приложения.

![Райдшеринг Uber](https://github.com/Zagalskiy/ml_web_app/raw/main/uber_demo.png "Райдшеринг Uber")

## Локальный запуск приложения:
```
pip install --upgrade streamlit
streamlit run https://raw.githubusercontent.com/Zagalskiy/ml_web_app/main/ml_web_app.py
```
