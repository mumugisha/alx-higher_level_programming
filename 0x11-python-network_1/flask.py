from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    email = request.form['email']
    return f'Received email: {email}'

if __name__ == '__main__':
    app.run(port=5000)
