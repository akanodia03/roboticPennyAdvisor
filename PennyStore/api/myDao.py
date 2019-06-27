import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="goodwill", database="penny_store")
class BillPayPaymentsDAO():

    def getPaymentDetails(paymentId):
        myCursor = mydb.cursor()
        myCursor.execute("select * from payments where PAYMENT_ID="+paymentId)
        result = myCursor.fetchall()
        myList = []
        for i in result:
            print(">>>>>>>>>>>>> "+i)
            myList.append(i)


        print(myList)
        return myList


    def setupPayments(self, paymentDetails):
        pass