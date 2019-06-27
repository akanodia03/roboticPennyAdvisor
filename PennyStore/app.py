from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)

if __name__ == "__main__":
    logger.debug("Starting you APP - PENNY_STORE")
    from api import *
    flaskAppInstance.run(debug=True)