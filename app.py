import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv("pelis.csv")


st.title("Peliculas")

#columnas en español
df = df.rename(columns={
    "Title": "Título",
    "Genre": "Género",
    "Director": "Director",
    "Actors": "Actores",
    "Year": "Año",
    "Runtime (Minutes)": "Duración (Minutos)",
    "Rating": "Calificación",
    "Votes": "Votos",
    "Revenue (Millions)": "Ingresos (Millones)",
    "Metascore": "Puntuación"
})

#tabla con las primeras 10 filas

st.write("Tabla con las primeras 10 filas:")
st.table(df.head(10))

#grafico de barras

st.write("Gráfico de barras:")
st.bar_chart(df["Género"].value_counts())

#grafico de torta

st.write("Gráfico de torta:")
st.write(df["Género"].value_counts().plot.pie(autopct="%1.1f%%"))

#grafico de lineas

st.write("Gráfico de líneas:")
st.line_chart(df["Año"].value_counts())

#grafico de area

st.write("Gráfico de área:")
st.area_chart(df["Año"].value_counts())

#grafico de dispersion

st.write("Gráfico de dispersión:")
st.write(alt.Chart(df).mark_circle().encode(
    x="Año",
    y="Duración (Minutos)",
    color="Género",
    tooltip=["Título", "Género", "Director", "Actores", "Año", "Duración (Minutos)", "Calificación", "Votos", "Ingresos (Millones)", "Puntuación"]
))

#grafico de barras apiladas

st.write("Gráfico de barras apiladas:")
st.write(alt.Chart(df).mark_bar().encode(
    x="Año",
    y="Duración (Minutos)",
    color="Género",
    tooltip=["Título", "Género", "Director", "Actores", "Año", "Duración (Minutos)", "Calificación", "Votos", "Ingresos (Millones)", "Puntuación"]
))

#grafico de barras apiladas horizontal

st.write("Gráfico de barras apiladas horizontal:")
st.write(alt.Chart(df).mark_bar().encode(
    x="Duración (Minutos)",
    y="Año",
    color="Género",
    tooltip=["Título", "Género", "Director", "Actores", "Año", "Duración (Minutos)", "Calificación", "Votos", "Ingresos (Millones)", "Puntuación"]
))

#top 5 peluculas mas votadas

st.write("Top 5 películas más votadas:")
st.table(df.sort_values("Votos", ascending=False).head(5))

#top 5 peluculas mejor calificadas

st.write("Top 5 películas mejor calificadas:")
st.table(df.sort_values("Calificación", ascending=False).head(5))

#top 5 peluculas mejor puntuadas

st.write("Top 5 películas mejor puntuadas:")
st.table(df.sort_values("Puntuación", ascending=False).head(5))

#actores mas populares

st.write("Actores más populares:")
st.table(df["Actores"].value_counts().head(5))

#directores mas populares

st.write("Directores más populares:")
st.table(df["Director"].value_counts().head(5))
















