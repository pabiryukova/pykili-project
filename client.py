import requests
import threading
import time

def printing(timestampp):
    while True:
        response = requests.get('http://127.0.0.1:5000/chat')
        data = response.json()

        for message in data['messages']:

            if message['timestamp'] > timestampp:
                if message['addressee'] in [username, 'all']:
                    print(message['username'], 'to', message['addressee'], ':', message['text'])
                    timestampp = message['timestamp']

        time.sleep(1)

    return timestampp


print('Введите имя:')
username = input()
print('Введите пароль:')
password = input()

response = requests.post(
    'http://127.0.0.1:5000/authorisation',
    json={'username': username, 'password': password})

print(response)

while data['ok'] != 'success':
    # пока сервер не сообщит, что логин и пароль верны, продолжаем попытки авторизации
    print('Неверное имя или пароль. Возможно, вы пытаетесь зайти под именем другого пользователя.')
    print('Повторно введите имя:')
    username = input()
    print('Повторно введите пароль:')
    password = input()

    response = requests.post(
        'http://127.0.0.1:5000/authorisation',
        json={'username': username, 'password': password})

    data = response.json()

x = threading.Thread(target=printing(0), daemon=True)
