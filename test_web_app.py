import requests # импорт запросов


def test_url():  # создаём функцию проверки работоспособности Web-приложения
    r = requests.head('https://nyc-uber.streamlit.app')
    assert r.status_code == 303  # проверяем статус код перенаправления
