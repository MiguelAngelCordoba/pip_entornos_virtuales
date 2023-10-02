import pandas

def get_population(df):
  population_dict = {
    # '2022': int(country_dict['2022 Population']),
    # '2020': int(country_dict['2020 Population']),
    # '2015': int(country_dict['2015 Population']),
    # '2010': int(country_dict['2010 Population']),
    # '2000': int(country_dict['2000 Population']),
    # '1990': int(country_dict['1990 Population']),
    # '1980': int(country_dict['1980 Population']),
    # '1970': int(country_dict['1970 Population'])
    '2022': df['2022 Population'].values,
    '2020': df['2020 Population'].values,
    '2015': df['2015 Population'].values,
    '2010': df['2010 Population'].values,
    '2000': df['2000 Population'].values,
    '1990': df['1990 Population'].values,
    '1980': df['1980 Population'].values,
    '1970': df['1970 Population'].values
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def conversor(dic):
  dic["2022"] = dic.pop('2022 Population')
  dic["2020"] = dic.pop('2020 Population')
  dic["2015"] = dic.pop('2015 Population')
  dic["2010"] = dic.pop('2010 Population')
  dic["2000"] = dic.pop('2000 Population')
  dic["1990"] = dic.pop('1990 Population')
  dic["1980"] = dic.pop('1980 Population')
  dic["1970"] = dic.pop('1970 Population')
  return dic



def population_by_country(data, country):
  result = data[data["Country"] == country]
  return result
