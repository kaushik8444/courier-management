import cx_Oracle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connect_exmp
import viewAll

def selectData(tabName,idName,id):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from {} where {} = {}'.format(tabName,idName,id))
    lst = cur.fetchone()
    conn.commit()
    conn.close()
    return lst

def updateEmp(empId,empName,empphone,empaddress,offid):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        update employee set EMP_NAME = :name, EMP_PHONE = :phone, EMP_ADDRESS = :addre, OFF_ID = :oid
        where EMP_ID = :eid""",
        eid=empId,name=empName,phone=empphone,addre=empaddress,oid=offid)
    conn.commit()
    conn.close()

def updateoff(offid,offname,offaddress):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update sections set OFF_NAME = :ONAME, OFF_ADDRESS = oadd
    where OFF_ID= :OID""",
    oid=offid,oname=offname,oadd=offaddress)
    conn.commit()
    conn.close()

def updateCus(cusId, cusName, cusphone, cusmail, cusaddress):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update customer set CUST_NAME = :name, CUS_PHONE = :cpho, CUS_EMAIL = :email,CUS_ADDRESS = :cadd
    where CUST_ID = :cid""",
    id=cusId, name=cusName, cpho=cusphone, email=cusmail, cadd=cusaddress)
    conn.commit()
    conn.close()

def updatecour(courId, courdesc,courtype,cusid,shipid):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update supplier set COUR_DESC = :cdes, COUR_TYPE = :cty, CUS_ID = :cid, SHIP_ID = :sid
    where COUR_ID = :coid""",
    coid=courId,cdes=courdesc,cty=courtype,cid=cusid,sid=shipid)
    conn.commit()
    conn.close()

def updateship(shipid,fromcity,tocity,offid):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        update cloth set FROM_CITY = :fcity, TO_CITY = :tcity,OFF_ID = :fid
        where SHIP_ID = :sid""",
        sid=shipid,fcity=fromcity,tcity=tocity,fid=offid)
    conn.commit()
    conn.close()
