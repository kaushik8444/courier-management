
import cx_Oracle
import sys

userName = 'kaushik'
password = '8522'

#create connection

try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:/Users/User/Documents/instantclient_21_3")
except Exception as err:
    print("Whoops!")
    print(err)
    sys.exit(1)

# conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
# print(conn.version)

# create cursor


# cur = conn.cursor()
# cur.execute("delete from employee where emp_id = {}".format(id))

def empLst():
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from employee")
    empLst = cur.fetchall()
    # print(empLst)
    return empLst

def offLst():
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from office")
    offLst = cur.fetchall()
    # print(offLst)
    return offLst

def cusLst():
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from customer")
    cusLst = cur.fetchall()
    # print(cusLst)
    return cusLst

def courLst():
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from courier")
    courLst = cur.fetchall()
    # print(courLst)
    return courLst

def shipLst():
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from shipment")
    shipLst = cur.fetchall()
    # print(shipLst)
    return shipLst



