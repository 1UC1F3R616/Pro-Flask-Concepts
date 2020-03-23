from flask import Flask
import os
from os import environ

app = Flask(__name__)
#app.config['HELLO'] = 'From file'
app.config['HELLO'] = environ.get('HELLO') # This will come from environment now


# bd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# app.config.from_pyfile(os.path.join(bd, 'config2', 'settings.py')) # Now taken from this file

@app.route('/')
def index():
    return app.config['HELLO']

if __name__ == "__main__":
    app.run()