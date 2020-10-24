from  flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = Flask(__name__)

db.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mabolong2006@localhost:3306/chat_wall"
db.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
db.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db.config['SQLALCHEMY_POOL_SIZE'] = 200
db.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
db.config['SQLALCHEMY_POOL_RECYCLE'] = 12

db = SQLAlchemy(db)