from flask import Flask, request
app = Flask(__name__)
messages = [{'username': 'jack', 'text': 'hello'}]

users= {}

@app.route('/')
def hello():
    return 'hello, world'

@app.route('/status')
def status():
    return {'status':True}
    
@app.route('/history')
def history():
    return {'messages': messages}

@app.route('/send', methods=['POST'])
def send():
    """ request = {'username': 'str'. 'password': 'str','text:'str''}
        response = {'ok': true}"""
    data = request.json
    username = data['username']
    text = data['text']
    password = data['password']
    
    if username in users:
        real_password = users[username]
        if real_password != password:
            return {'ok': False}
        else:
            users[username] = password
            
        new_message = {'username' : username, 'text' : text}
        messages.append(new_message)

        return {'ok' : True}
    else:
        return {'ok': False}
if __name__ == "__main__":
    app.run()
