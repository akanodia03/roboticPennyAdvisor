import mysql.connector

import datetime, time


def run_sql_file(filename, connection):
    '''
    The function takes a filename and a connection as input
    and will run the SQL query on the given connection
    '''
    start = time.time()

    file = open(filename, 'r')
    sql = s = " ".join(file.readlines())
    print
    "Start executing: " + filename + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + "\n" + sql
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

    end = time.time()
    print
    "Time elapsed to run the query:"
    print
    str((end - start) * 1000) + ' ms'


def main():
    connection = mysql.connector.connect(host="localhost", user="root", passwd="goodwill")
    run_sql_file("ddlScript.sql", connection)
    connection.close()


if __name__ == "__main__":
    main()