# 📈 Cuadro de mandos personal 📊

> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo

El objetivo de este proyecto es diseñar un cuadro de mandos personal para la visualización e interacción con un conjunto de datos de películas.

## Los datos

Para este proyecto se ha utilizado un conjunto de datos de películas que se ha obtenido a través del portal de datos abiertos Kaggle. El conjunto de datos contiene información sobre 1000 películas, incluyendo su género, actores, director, votos y más.

## Búsqueda de los datos

Busca una fuente para tus datos. Puedes usar una API de un portal de datos abiertos, un conjunto ya publicado, recopilar personalmente datos por scraping, etc.

## Documentación de los datos

Los datos utilizados en este proyecto provienen del conjunto de datos "Peliculas". El conjunto de datos ha sido obtenido a través del portal de datos abiertos Kaggle. Cada fila en el conjunto de datos representa una película y contiene información como el título, el género, el director, los actores, el año de estreno, el idioma, la duración, la clasificación, la recaudación y más.

## Prepara tu aplicación.

La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.

Para preparar la aplicación se ha creado un archivo llamado app.py que utiliza las siguientes dependencias:

Pandas: para cargar y analizar el conjunto de datos.
Streamlit: para diseñar la aplicación interactiva.
Matplotlib y Seaborn: para visualizar los datos.

## Carga y análisis de conjunto de dato con pandas

El conjunto de datos se ha cargado en un dataframe de pandas y se ha realizado un análisis de los datos. Se han utilizado las funciones básicas de pandas para analizar los datos, como head(), describe(), value_counts() y más. También se han eliminado las columnas innecesarias del conjunto de datos.

## Visualización de los datos

Se han creado varias visualizaciones diferentes del dataframe utilizando las librerías Matplotlib y Seaborn. Se han utilizado gráficos de barras, histogramas y diagramas de dispersión para visualizar la información de las películas, como la recaudación y la duración de las mismas.

## Diseña la interacción que van a tener tus datos

La interacción con los datos se ha diseñado mediante la selección de opciones de menú y la selección de valores en cuadros de entrada. La aplicación permite al usuario filtrar las películas por género, actor y director. También se pueden ordenar las películas por año de estreno, recaudación y votos.

## Prepara la aplicación (cuadro de mandos) con Streamlit

Se ha diseñado la aplicación interactiva utilizando la librería Streamlit. Se han creado menús desplegables y cuadros de entrada para permitir al usuario interactuar con los datos.

## Publica la aplicación.

Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app

## CONCLUSION

En conclusión, este proyecto me ha permitido aplicar los conocimientos adquiridos en el análisis y visualización de datos mediante el uso de la librería Pandas y las herramientas de visualización como Matplotlib y Altair. Además, he aprendido cómo utilizar Streamlit para diseñar una aplicación interactiva y fácil de usar para la exploración de datos.

En cuanto a mi opinión personal, creo que este proyecto ha sido muy útil para mí ya que he aprendido mucho sobre el procesamiento de datos y visualización. Me ha permitido aplicar de manera práctica los conceptos teóricos aprendidos en el grado y, además, he adquirido nuevas habilidades en el uso de herramientas para la visualización de datos.

En resumen, este proyecto ha sido una excelente oportunidad para adquirir experiencia práctica en el análisis de datos y visualización, lo que me será muy útil en mi carrera profesional en el futuro.
