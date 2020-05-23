import requests
from bs4 import BeautifulSoup
import datetime
'''
Создать консольную программу-парсер, с выводом прогноза погоды. Дать
возможность пользователю получить прогноз погоды в его локации ( по
умолчанию) и в выбраной локации, на определенную пользователем дату.
Можно реализовать, как консольную программу, так и веб страницу.
Используемые инструменты: requests, beatifulsoup, остальное по желанию.
На выбор можно спарсить страницу, либо же использовать какой-либо API.
'''


def weather_default(day_delta=0):
    url = 'https://sinoptik.ua'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    name = soup.select('.cityName')
    weather = soup.findAll('div', {'class': 'temperature'})
    print(f'\n{name[0].getText()}, {weather[day_delta].getText()}')


def change_weather(city, day, day_delta):
    url = f'https://sinoptik.ua/погода-{city}/{day}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    name = soup.select('.cityName')
    weather = soup.findAll('div', {'class': 'temperature'})
    get_info = soup.select('.description')
    print(f'\n{name[0].getText()}, {weather[day_delta].getText()}')
    print(f'Info: {get_info[0].getText()}')
    return city, day, day_delta


print('Welcome to simple sinoptik weather')
weather_default()
while True:
    step = input('Enter a day or a city where you want to see a weather\nOr exit to exit: \n ')

    if step == 'exit':
        print('Have a nice day, goodbye')
        break

    if step.isdigit():
        day_delta = int(step) - datetime.date.today().day
        weather_default(int(day_delta))
        continue

    elif step.isalpha():
        day = int(input('Enter a day: '))
        month = int(input('Enter a month: '))
        use_day = datetime.date(datetime.date.today().year, month, day).strftime('%Y-%m-%d')
        day_delta = day - datetime.date.today().day
        try:
            change_weather(step, use_day, day_delta)
        except IndexError as error:
            print('Error: You can choice a weather not more then 5 days')
        else:
            continue
