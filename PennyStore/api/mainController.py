from flask_restful import Resource
import logging as logger

class myController(Resource):

    def addPayment(self):
        logger.debug("inside setupPayment method")
        return {"message":"Inside post method"},200

    def paymentDetails(self):
        logger.debug("inside paymentDetails method")
        return {"message": "Inside get method"}, 200
    def updatePayment(self):
        logger.debug("inside updatePayment method")
        return {"message": "Inside put method"}, 200
    def deletePayment(self):
        logger.debug("inside deletePayment method")
        return {"message": "Inside delete method"}, 200