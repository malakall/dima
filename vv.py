import requests
import pandas as pd

def get_vacancies(skills, pages=10):
    res = []
    for indx, skill in enumerate(skills):
        print(f'\ncollecting <{skill}> ({indx+1} of {len(skills)})')
        for page in range(pages):
            params = {
                'text': f'{skill}',
                'page': page,
                'per_page': 100,
                'only_with_salary': 'true',
            }
            req = requests.get('https://api.hh.ru/vacancies/', params).json()
            if 'items' in req.keys():
                res.extend(req['items'])
            print('|', end='')
    return res

def is_programming_related(title):
    programming_keywords = [
        'программист', 'разработчик', 'developer', 'software', 'engineer', 'programmer'
    ]
    title_lower = title.lower()
    return any(keyword in title_lower for keyword in programming_keywords)

# Ваши навыки
skills = ['skill_1', 'skill_2']

# Сбор данных о вакансиях
vacancies_data = get_vacancies(skills)

# Создание DataFrame
df = pd.DataFrame(vacancies_data)

# Фильтрация данных
df_filtered = df[df['name'].apply(is_programming_related)]

# Сохранение исходных данных в CSV
df.to_csv('vacancies.csv', index=False)

# Сохранение отфильтрованных данных в новый CSV-файл
df_filtered.to_csv('filtered_vacancies.csv', index=False)

print("Данные собраны и отфильтрованы. Исходные данные сохранены в 'bom.csv'. Отфильтрованные данные сохранены в 'filtered_vacancies.csv'.")
