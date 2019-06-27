import mysql.connector
from datetime import datetime
import random
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="goodwill",
    database="penny_store")
class BillPayPaymentsDAO():

    def getPaymentDetails(paymentId):
        myCursor = mydb.cursor()
        myCursor.execute("select * from payments where PAYMENT_ID=1234")
        result = myCursor.fetchall()
        mydb.close
        return result.__getitem__(0)


    def setupPayments(creditAccountId, debitAccountId, memo):
        mycursor = mydb.cursor()
        sql = "INSERT INTO payments (" \
              "PAYMENT_ID," \
              "CREDIT_ACCOUNT_ID," \
              "DEBIT_ACCOUNT_ID," \
              "TRANSACTION_DATE," \
              "MEMO) VALUES (%s, %s, %s, %s, %s)"

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        paymentId = random.randint(1000, 10000)
        val = (paymentId, creditAccountId, debitAccountId,formatted_date, memo)
        mycursor.execute(sql, val)

        mydb.commit()

        mydb.close
        return paymentId
