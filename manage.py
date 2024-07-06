from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import csv

# Функция для загрузки данных из CSV файла
def load_data_from_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Функция для отображения данных
def show_data(data):
    if data:
        header = list(data[0].keys())
        rows = [list(row.values()) for row in data]
        put_table([header] + rows)
    else:
        put_text("Нет данных для отображения")

# Определяем путь к файлу CSV
csv_file_path = 'vacancies.csv'

# Загружаем данные из CSV файла
data = load_data_from_csv(csv_file_path)

# Создаем интерфейс фильтрации данных
def filter_data_interface():
    while True:
        choice = radio("Выберите поле для фильтрации:", options=['name', 'salary'])
        
        if choice == 'name':
            name_filter = input("Введите часть названия вакансии для фильтрации:")
            filtered_data = [row for row in data if name_filter.lower() in row['name'].lower()]
            show_data(filtered_data)
        elif choice == 'salary':
            salary_filter = input("Введите минимальную зарплату для фильтрации:", type=NUMBER)
            filtered_data = [row for row in data if row['salary'] and int(row['salary']) >= salary_filter]
            show_data(filtered_data)

        cont = actions(label="Продолжить фильтрацию?", buttons=['Да', 'Нет'])
        if cont == 'Нет':
            break

# Запускаем веб-приложение
start_server(filter_data_interface, port=8080)