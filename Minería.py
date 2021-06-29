from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('netflix_titles.csv')

#----------------------------------Mandatos/Respuestas----------------------------------#
# 1. Cargar el archivo 'netflix_titles.csv'.
# data = pd.read_csv('./netflix_titles.csv')
# print(data)
#--------------------------------------------------------------#
# 2. Visualizar los primeros 10 registros del conjunto de datos.
# print(data.head(10))
#--------------------------------------------------------------#
# 3. Visualizar los últimos 15 registros del conjunto de datos.
# print(data.tail(15))
#--------------------------------------------------------------#
# 4. Generar los estadísticos básicos.
# print(data.describe())
#--------------------------------------------------------------#
# 5. Completar todos los datos vacíos (na) con ceros (0).
# print(data.fillna(0))
#--------------------------------------------------------------#
# 6. Generar un gráfico de tipo 'scatter' utilizando la variable "release_year" en el eje X y la variable "type_id" en el Eje Y.
# print(set(data.release_year))
# print(set(data.type_id))
# fig, ax = plt.subplots()
# ax.scatter(data.release_year, data.type_id)
# plt.show()