[![Tests](https://github.com/Zagalskiy/ml_web_app/actions/workflows/python-app.yml/badge.svg)](https://github.com/Zagalskiy/ml_web_app/actions/workflows/python-app.yml)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nyc-uber.streamlit.app/)

# Web-приложение на основе библиотеки Streamlit: райдшеринг Uber в Нью-Йорке

Демонстрационное Web-приложение [Streamlit](https://streamlit.io) [написанное на чистом Пайтоне](https://github.com/Zagalskiy/ml_web_app/blob/main/ml_web_app.py) для интерактивной визуализации подачи машин райдшеринга Uber в Нью-Йорке и в его крупных аэропортах с течением времени.

Используются библиотеки:
- Altair(библиотека статической визуализации, основанная на граммматиках визуализации Vega и Vega-Lite)
- Numpy(Open-source модуль, представляющий общие математические и числовые операции в виде прескомпилированных, быстрых функций)
- Pandas(Библиотека для обработки и анализа данных)
- Pydeck(Библиотека для создания гибко настраиваемых многолойных графиков)
- Streamlit(Фреймворк для развертывания моделей машинного обучения в Web-приложениях)

Репозиторий проекта состоит из следующих файлов:
- [Readme.md](https://github.com/Zagalskiy/ml_web_app/blob/main/README.md)- описание проекта
- [ml_web_app.py](https://github.com/Zagalskiy/ml_web_app/blob/main/ml_web_app.py)- код модели машиннго обучения
- [requirements.txt](https://github.com/Zagalskiy/ml_web_app/blob/main/requirements.txt)- список библиотек для установки
- [test_web_app.py](https://github.com/Zagalskiy/ml_web_app/blob/main/test_web_app.py)- тест проверки работоспособности приложения
- [uber-raw-data-sep14.csv.gz](https://github.com/Zagalskiy/ml_web_app/blob/main/uber-raw-data-sep14.csv.gz)- датасет с координатами передвижения машин
- [uber_demo.png](https://github.com/Zagalskiy/ml_web_app/blob/main/uber_demo.png)- картинки для визуализации
- [workflows](https://github.com/Zagalskiy/ml_web_app/tree/main/.github/workflows)- файл автоматизированного запуска тестов Continuous Integration


Тестирует GitHub Actions и проверяет работоспособность Web-приложения.

![Райдшеринг Uber](https://github.com/Zagalskiy/ml_web_app/raw/main/uber_demo.png "Райдшеринг Uber")

## Локальный запуск приложения:
```
pip install --upgrade streamlit
streamlit run https://raw.githubusercontent.com/Zagalskiy/ml_web_app/main/ml_web_app.py
```
Над созданием проекта работали:
* Загальский И.К.
* Мурейко Е.С.
* Санникова Ю.И.
* Майнгерт В.А.