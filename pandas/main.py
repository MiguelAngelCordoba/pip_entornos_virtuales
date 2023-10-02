import utils
import read_csv
import plot
import pandas 

def run():

  dataframe = pandas.read_csv('data.csv')      # lee el csv y directamente me lo convierte en diccionario
  df = dataframe[dataframe['Continent'] == 'Africa']      # es la forma de filtrar por columnas, en este caso filtramos segun el continente

  countries = df['Country'].values        # guardamos los valores de la columna Country, es decir en este caso guardamos los nombres de los paises
  percentages = df['World Population Percentage'].values    # guardamos los valores de esa columna
  plot.generate_pie_chart(countries, percentages)

  pais = input('Elije un pais para ver su crecimiento poblacional: ')

  result = utils.population_by_country(dataframe, pais)
  
  if len(result) > 0:

    indice_pais = dataframe[dataframe['Country'] == pais].index[0]    # cuadamos en que fila esta el pais indicado

    # Define las columnas cuyos valores deseas incluir en el diccionario
    columnas_deseadas = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']

    # Crea un diccionario con los valores de las columnas deseadas para la fila 'pais'
    fila_dict = {columna: dataframe.at[indice_pais, columna] for columna in columnas_deseadas}
    
    poblacion_años = utils.conversor(fila_dict)    # quitamos la palabra Population a los años para graficar mejor

    llaves = list(poblacion_años.keys())
    valores = list(poblacion_años.values())
    plot.generate_bar_chart(pais, llaves, valores)

if __name__ == '__main__':
  run()
