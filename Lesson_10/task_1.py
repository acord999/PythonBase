import pandas as pd

# Создание исходного набора данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Создание столбцов one-hot кодирования с помощью метода get_dummies
one_hot_encoding = pd.get_dummies(data['whoAmI'])

# Объединение исходных данных с one-hot кодированием
data_encoded = pd.concat([data, one_hot_encoding], axis=1)

data_encoded.head()
