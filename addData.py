import cx_Oracle

def addEmployee(empId,empName,empphone,empaddress,offid):
    # print(empId + " " + empName + " " + empphone + " " + empaddress + " " + offid)
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        insert into employee (EMP_ID, EMP_NAME, EMP_PHONE,EMP_ADDRESS,OFF_ID) 
        values (:id, :name, :ephone, :addre, :oid)""",
        id=empId, name=empName, ephone=empphone, addre=empaddress,oid=offid)
    conn.commit()
    conn.close()

def addoffice(offid,offname,offaddress):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into office (OFF_ID,OFF_NAME,OFF_ADDRESS)
    values (:oid, :oname, :oadd)""",
    oid=offid,oname=offname,oadd=offaddress)
    conn.commit()
    conn.close()

def addCustomer(cusId, cusName, cusphone, cusemail, cusaddress):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into customer (CUST_ID, CUST_NAME, CUS_PHONE, CUS_EMAIL, CUS_ADDRESS)
    values (:cid, :cname, :cpho, :email, :cadd)""",
    cid=cusId, cname=cusName, cpho=cusphone, email=cusemail, cadd=cusaddress)
    conn.commit()
    conn.close()

def addcourier(courid,courdesc,courtype,cusid,shipid):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into supplier (COUR_ID,COUR_DESC,COUR_TYPE,CUS_ID,SHIP_ID)
    values (:coid, :cdesc, :ctype, :cid, :sid)""",
    coid=courid,cdesc=courdesc,ctype=courtype,cis=cusid,sid=shipid)
    conn.commit()
    conn.close()

def addshipment(shipid,fromcity,tocity,offid):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        insert into shipment(SHIP_ID,FROM_CITY,TO_CITY,OFF_ID) 
        values (:sid, :fcity, :tcity, :oid)""",
        sid=shipid,fcity=fromcity,tcity=tocity,oid=offid)
    conn.commit()
    conn.close()