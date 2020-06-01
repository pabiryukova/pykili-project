from flask import Flask, request
import time

app = Flask(__name__)
messages = []
users = {}  # {'username':password}


@app.route('/')
def hello():
    return 'Добро пожаловать в чат!'


@app.route('/authorisation', methods=['POST'])
# request = {'username': str, 'password': str}
def autho():
    data = request.json
    username = data['username']
    password = data['password']
    for key in users:
        if username == key:
            if password == users[username]:
                return {'ok': success}
            else:
                return {'ok': error}
        else:
            users[username] = password
            return {'ok': success}


@app.route('/chat')
def chat():
    return {'chat': messages}


@app.route('/send', methods=['POST'])
# request = {'username': str, 'addressee' = str, 'text' = str}
def send():
    data = request.json
    username = data['username']
    addressee = data['addressee']
    text = data['text']
    timestamp = time.ctime()

    new_message = {'username': username, 'addressee': addressee, 'text': text, 'timestamp': timestamp}
    messages.append(new_message)

    return {'ok': success}


if __name__ == '__main__':
    app.run()
