import pandas as pd

# Загрузить данные из CSV файла
input_filename = 'Phones_list.csv'
output_filename = 'Result_list.csv'

# Чтение CSV файла в DataFrame
df = pd.read_csv(input_filename)

# Функция для очистки номеров телефонов
def clean_phone_number(phone_number):
    # Оставить только цифры
    digits = ''.join(filter(str.isdigit, str(phone_number)))
    # Проверить, что номер содержит 8 цифр
    if len(digits) == 8:
        return digits
    else:
        return None  # Возвращаем None для удаления неправильных номеров

# Применить функцию очистки к столбцу с номерами телефонов
df['Phone'] = df['Phone'].apply(clean_phone_number)

# Удаляем пустые
df.dropna(inplace=True)

# Удалить дубликаты
df.drop_duplicates(subset=['Phone'], inplace=True)
# Перенумеровка
df['Id'] = range(1, len(df) + 1)


# Сохранить результат в новый CSV файл
df.to_csv(output_filename, index=False)



