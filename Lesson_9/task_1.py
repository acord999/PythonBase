import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Фильтрация данных по количеству людей от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вывод информации о цене дома
print("Максимальное значение цены дома:", filtered_data['median_house_value'].max())
print("Минимальное значение цены дома:", filtered_data['median_house_value'].min())
print("Среднее значение цены дома:", filtered_data['median_house_value'].mean())
print("Медиана цены дома:", filtered_data['median_house_value'].median())