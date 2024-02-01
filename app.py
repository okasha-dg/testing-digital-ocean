from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    branch_name = os.getenv('BRANCH_NAME', 'main')
    return f'Hello, World! This is the {branch_name} branch.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)