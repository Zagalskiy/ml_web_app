import altair as alt  # - для построения линейных графиков
import numpy as np  # - для математических и числовых операций
import pandas as pd  # - для обработки и анализа данных
import pydeck as pdk  # - для создания визулизации данных
import streamlit as st  # - фреймворк для развертывания моделей и визуализаций

# Задание широкоформатного режима страницы и указание заголовка
st.set_page_config(layout="wide", page_title="Демо райдшеринга в Нью-Йорке",
                   page_icon=":taxi:")


# Загрузка исходных данных
@st.experimental_singleton   # Функция декоратора для хранения одноэлементных объектов
def load_data():  # предназначенная для избежания повторного пересчета
    data = pd.read_csv(
        "uber-raw-data-sep14.csv.gz",
        nrows=100000,  # ограничение объема исходных данных 10 %
        names=[
            "date/time",
            "lat",
            "lon",
        ],
        skiprows=1,
        usecols=[0, 1, 2],  # исключаем из таблицы столбец с константой "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )
    return data


def map(data, lat, lon, zoom):  # Задание функции для определения областей на карте.
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/outdoors-v12",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=54,  # Задание радиуса точки подбора
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )


# Фильтрация данных с часовым интервалом
@st.experimental_memo
def filter_by_data(df, hour_selected):
    return df[df["date/time"].dt.hour == hour_selected]


# Вычисление средней величины для полученного набора данных
@st.experimental_memo
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))


# Фильтрация данных по часам
@st.experimental_memo
def histdata(df, hr):
    filtered = data[
        (df["date/time"].dt.hour >= hr) & (df["date/time"].dt.hour < (hr + 1))
    ]
    hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0, 60))[0]
    return pd.DataFrame({"minute": range(60), "pickups": hist})


# Макет приложения STREAMLIT
data = load_data()

# Построение верхнего уровня визуализации
row1_1, row1_2 = st.columns((2, 3))

# Проверка на наличие параметра в URL, определяющего время пользователя (например, "?pickup_hour=2")
# и позволяющего задать его время в приложении, например
# https://nyc-uber.streamlit.app/?pickup_hour=0
if not st.session_state.get("url_synced", False):
    try:
        pickup_hour = int(st.experimental_get_query_params()["pickup_hour"][0])
        st.session_state["pickup_hour"] = pickup_hour
        st.session_state["url_synced"] = True
    except KeyError:
        pass


def update_query_params():  # Обновление параметра запроса при изменении положения ползунка
    hour_selected = st.session_state["pickup_hour"]
    st.experimental_set_query_params(pickup_hour=hour_selected)


with row1_1:
    st.title("Данные райдшеринга Uber в Нью-Йорке")
    hour_selected = st.slider(
        "Выберите час подачи", 0, 23, key="pickup_hour", on_change=update_query_params
    )

with row1_2:
    st.write(
        """
    ##
    Визуализация изменения подачи машин райдшеринга Uber в Нью-Йорке и в его крупных аэропортах с течением времени.
    Перемещая ползунок слева, можно изучать различные тенденции в развитии транспорта в разные интервалы времени.
    """
    )

# Установка местоположения масштабирования для аэропортов
zoom_level = 12
midpoint = mpoint(data["lat"], data["lon"])

# Построение среднего уровня визуализации
st.write(
        f"""**Весь Нью-Йорк от {hour_selected}:00 до {(hour_selected + 1) % 24}:00**"""
)
map(filter_by_data(data, hour_selected), midpoint[0], midpoint[1], 11)

# Построение нижнего уровня визуализации
row3_1, row3_2, row3_3 = st.columns((1, 1, 1))

# Установка местоположения масштабирования для аэропортов
la_guardia = [40.7900, -73.8700]
jfk = [40.6650, -73.7821]
newark = [40.7090, -74.1805]
zoom_level = 12
midpoint = mpoint(data["lat"], data["lon"])

with row3_1:
    st.write("**Аэропорт Ла Гуардиа**")
    map(filter_by_data(data, hour_selected), la_guardia[0], la_guardia[1], zoom_level)

with row3_2:
    st.write("**Аэропорт им. Дж. Кеннеди**")
    map(filter_by_data(data, hour_selected), jfk[0], jfk[1], zoom_level)

with row3_3:
    st.write("**Аэропорт Ньюарк**")
    map(filter_by_data(data, hour_selected), newark[0], newark[1], zoom_level)

# Расчет данных для гистограммы
chart_data = histdata(data, hour_selected)

# Разметка раздела гистограммы
st.write(
    f"""**Подробная поминутная раскладка поездок в период между {hour_selected}:00 и {(hour_selected + 1) % 24}:00**"""
)


st.altair_chart(
    alt.Chart(chart_data)
    .mark_area(
        color="lightblue",
        interpolate='step-after',
        line=True
    )
    .encode(
        x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
        y=alt.Y("pickups:Q"),
        tooltip=["minute", "pickups"],
    )
    .configure_mark(opacity=0.3, color="purple"),
    use_container_width=True,
)
