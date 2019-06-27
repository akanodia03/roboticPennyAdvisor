from flask_restful import Api
from app import flaskAppInstance
from .mainController import myController

restServer = Api(flaskAppInstance)

restServer.add_resource(myController,resource="")