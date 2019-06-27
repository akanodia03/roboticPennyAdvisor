from flask_restful import Resource
import logging as logger

class HelloWorldController(Resource):

    def helloWorld(self,name):
        logger.debug("inside setupPayment method")
        return {"message":"Inside post method"+name},200