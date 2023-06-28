import pandas as pd

# Загрузка данных из файла california_housing_train.csv
data = pd.read_csv('sample_data/california_housing_train.csv')

# Находим минимальное значение population
min_population = data['population'].min()

# Фильтруем данные по минимальному значению population
min_population_data = data[data['population'] == min_population]

# Находим максимальное значение households в данных с минимальным значением population
max_households = min_population_data['households'].max()

print("Максимальное значение households в зоне минимального значения population:", max_households)

