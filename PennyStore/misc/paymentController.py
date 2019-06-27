from flask_restful import Resource
import logging as logger



class PaymentController(Resource):


    def addPayment(self):
        logger.debug("inside setupPayment method")
        return {"message":"Inside post method"},200


    def paymentDetails(paymentId):
        logger.debug("inside paymentDetails method")
        return {"message": "Inside get method"+paymentId}, 200


    def updatePayment(self):
        logger.debug("inside updatePayment method")
        return {"message": "Inside put method"}, 200


    def deletePayment(paymentId):
        logger.debug("inside deletePayment method")
        return {"message": "Inside delete method"+paymentId}, 200


    def helloWorld(self):
        return 'Hi, How are you. Welcome to Penny Store'
