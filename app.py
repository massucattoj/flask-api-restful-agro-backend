import os

from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from db import db
from resources.loss_communication import (LossCommunication,
                                          LossCommunicationList)

app = Flask(__name__)
swagger = Swagger(app)

app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", "sqlite:///data.db") # tell where is the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI", "SQLALCHEMY_DATABASE_URI") # tell where is the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # specify configuration property

api = Api(app)


# Add the resources
api.add_resource(LossCommunicationList, '/loss_communication')
api.add_resource(LossCommunication, '/loss_communication/<int:id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
