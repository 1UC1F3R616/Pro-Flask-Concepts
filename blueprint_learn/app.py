from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getcwd, environ
from os.path import join

app = Flask(__name__)
app.config['DEBUG']=True

# if __name__ == "__main__":
#     print('Call from file: ' + str(__file__))
# else:
#     print('Call from Another File')

PATH_TO_CONFIG = join(getcwd(), 'config.py')
app.config.from_pyfile(PATH_TO_CONFIG)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

PG = environ.get("DATABASE_URL")
PATH_TO_LOCAL_DB = join(getcwd(), 'db.sqlite')
if PG is None or PG=="":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        PATH_TO_LOCAL_DB
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = PG

db = SQLAlchemy(app)


# Importing Models
from auth.auth import auth_bp

# Registring Models
app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__ == "__main__":
    app.run()