from flask_script import Manager
from flask import Flask
from flask import redirect

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
 return redirect('http://www.example.com')

if __name__ == '__main__':
 manager.run()