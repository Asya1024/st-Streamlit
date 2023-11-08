import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Заголовок приложения
st.title('Сайт Анализ Стран')

# Создание вкладки "Загрузка Excel-файла"
st.sidebar.header("Загрузка Excel-файла")
uploaded_file = st.sidebar.file_uploader("Загрузите файл Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Чтение данных из Excel-файла
    xls = pd.ExcelFile(uploaded_file)

    # Предполагаем, что данные находятся на первом листе (вы можете изменить это, если данные находятся на другом листе)
    df = xls.parse(xls.sheet_names[0])

    # Удалите столбец с именем "Год" (замените его на имя вашего столбца)
    if "Год" in df.columns:
        df = df.drop(columns=["Год"])

    # Отображение данных в виде таблицы
    st.dataframe(df)

    # Создание графика на основе данных (первый график - точечная диаграмма)
    st.write("### График данных (Точечная диаграмма)")
    x_col = st.sidebar.selectbox("Выберите столбец для оси X", df.columns)
    y_col = st.sidebar.selectbox("Выберите столбец для оси Y", df.columns)
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], marker='o')  # Используйте plt.scatter для точечной диаграммы
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    st.pyplot(plt)

    # Создание второго графика на основе данных (второй график - линейная диаграмма с точками)
    st.write("### График данных (Линейная диаграмма с точками)")
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[y_col], marker='o')  # Используйте plt.plot для линейной диаграммы с точками
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    st.pyplot(plt)
