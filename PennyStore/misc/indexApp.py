from flask import Flask
import logging as logger
from flask_restful import Api
from misc.paymentController import PaymentController
from misc.helloWorldController import HelloWorldController

logger.basicConfig(level="DEBUG")

instance = Flask(__name__)
api = Api(instance)

api.add_resource(PaymentController,'/payments/', endpoint='payments')
api.add_resource(HelloWorldController, '/hello/<string:id>', endpoint='hello')

if __name__ == "__main__":
    logger.debug("Starting your APP - PENNY_STORE")
    instance.run(debug=True)