from flask import Flask,request
from flask import jsonify
from api.myDao import BillPayPaymentsDAO
import random
app = Flask(__name__)


@app.route("/v1/pennyStotre/add", methods=["POST"])
def addPayment():
    data = request.get_json()
    creditAccountId = data["creditAccountId"]
    debitAccountId = data["debitAccountId"]
    memo = data["memo"]
    paymentId = \
        BillPayPaymentsDAO.setupPayments(creditAccountId, debitAccountId, memo)
    d ={"paymentId":paymentId}
    return jsonify(d)

@app.route("/v1/pennyStotre/activity/<paymentId>", methods=["GET"])
def getPaymentDetails(paymentId):
    paymentDetails = BillPayPaymentsDAO.getPaymentDetails(paymentId)
    paymentId = paymentDetails[0]
    creditAccountId = paymentDetails[1]
    debitAccountId = paymentDetails[2]
    date = paymentDetails[3]
    memo = paymentDetails[4]
    d ={
    "paymentId":paymentId,
    "creditAccountId":creditAccountId,
    "debitAccountId":debitAccountId,
    "memo":memo
    }
    return jsonify(d);

@app.route("/v1/pennyStotre/update", methods=["PUT"])
def updatePayment(self):
    return "Hello World"

@app.route("/v1/pennyStotre/cancel/<paymentId>", methods=["DELETE"])
def deletePayment(paymentId):
    return "Hello World"

@app.route("/")
def allUri():
    d= {
        "/v1/pennyStotre/add":"POST",
        "/v1/pennyStotre/activity/<paymentId>": "GET",
        "/v1/pennyStotre/update": "PUT",
        "/v1/pennyStotre/cancel/<paymentId>": "DELETE"
    }
    return jsonify(d)

if __name__=="__main__":
    app.run(debug=True)