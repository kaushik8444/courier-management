from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connect_exmp
import addData



# Add Employee
def addEmp():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(empIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
            empId = empIdEtr.get()
        if(empNameEtr.get() == ''):
            empName = ''
        else:
            empName = empNameEtr.get()
        if(empphoneEtr.get() == ''):
            empphone = ''
        else:
            empphone = empphoneEtr.get()
        if(empaddressEtr.get() == ''):
            empaddress = ''
        else:
            empaddress = empaddressEtr.get()
        if(offIdEtr.get() == ''):
            offid = ''
        else:
            offid = offIdEtr.get()
        
        
        addData.addEmployee(empId,empName,empphone,empaddress,offid)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    window.winfo_screenwidth()
    window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Employee")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Employee ID:",padding=10).grid(column=0, row=0)
    empIdEtr = Entry(frm)
    empIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Employee Name:",padding=10).grid(column=0, row=1)
    empNameEtr = Entry(frm)
    empNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="employee phone:",padding=10).grid(column=0, row=2)
    empphoneEtr = Entry(frm)
    empphoneEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="employee address:",padding=10).grid(column=0, row=3)
    empaddressEtr = Entry(frm)
    empaddressEtr.grid(column = 1, row = 3 )

    ttk.Label(frm, text="office Id:",padding=10).grid(column=0, row=4)
    offIdEtr = Entry(frm)
    offIdEtr.grid(column = 1, row = 4)


    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=8)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=8)

    window.mainloop()

# Add ofice
def addOff():

    def cancelBtn():
        window.destroy()

    def addBtn():

        if(offIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Section No cannot be Empty')
        else:
            offid= offIdEtr.get()
        
        if(offnameEtr.get() == ''):
            offname = ''
        else:
            offname = offnameEtr.get()
        
        if(offaddressEtr.get() == ''):
            offaddress = ''
        else:
            offaddress = offaddressEtr.get()
        
        addData.addoffice(offid,offname,offaddress)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    window.winfo_screenwidth()
    window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New office place")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="office Id:",padding=10).grid(column=0, row=0)
    offIdEtr = Entry(frm)
    offIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="office name:",padding=10).grid(column=0, row=1)
    offnameEtr = Entry(frm)
    offnameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="office address:",padding=10).grid(column=0, row=2)
    offaddressEtr = Entry(frm)
    offaddressEtr.grid(column = 1, row = 2)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=4)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=4)

    window.mainloop()

# Add Customer
def addCus():

    def cancelBtn():
        window.destroy()

    def addBtn():

        if(cusIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Customer ID cannot be Empty')
        else:
            cusId = cusIdEtr.get()
        if(cusNameEtr.get() == ''):
            cusName = ''
        else:
            cusName = cusNameEtr.get()
        if(cusphoneEtr.get() == ''):
            cusphone = ''
        else:
            cusphone = cusphoneEtr.get()
        if(cusemailEtr.get() == ''):
            cusemail = ''
        else:
            cusemail = cusemailEtr.get()
        if(cusaddressEtr.get() == ''):
            cusaddress = ''
        else:
            cusaddress = cusaddressEtr.get()

        addData.addCustomer(cusId, cusName, cusphone, cusemail, cusaddress)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    window.winfo_screenwidth()
    window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Customer")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Customer ID:",padding=10).grid(column=0, row=0)
    cusIdEtr = Entry(frm)
    cusIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Customer Name:",padding=10).grid(column=0, row=1)
    cusNameEtr = Entry(frm)
    cusNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="customer phone:",padding=10).grid(column=0, row=2)
    cusphoneEtr = Entry(frm)
    cusphoneEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="customer email:",padding=10).grid(column=0, row=3)
    cusemailEtr = Entry(frm)
    cusemailEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="customer address:",padding=10).grid(column=0, row=4)   
    cusaddressEtr = Entry(frm)
    cusaddressEtr.grid(column = 1, row = 4 )

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)

    window.mainloop()

# Add Cour
def addCour():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(couridEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
            courid = couridEtr.get()
        if(courdescEtr.get() == ''):
            courdesc = ''
        else:
            courdesc = courdescEtr.get()
        if(courtypeEtr.get() == ''):
            courtype = ''
        else:
            courtype = courtypeEtr.get()
        if(cusidEtr.get() == ''):
            cusid = ''
        else:
            cusid = cusidEtr.get()
        if(shipidEtr.get() == ''):
            shipId = ''
        else:
            shipId = shipidEtr.get()
        

        addData.addcourier(courid, courdesc, courtype, cusid, shipId)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    window.winfo_screenwidth()
    window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New courier")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields

    ttk.Label(frm, text="Courier Id:",padding=10).grid(column=0, row=0)
    couridEtr = Entry(frm)
    couridEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Courier description:",padding=10).grid(column=0, row=1)
    courdescEtr = Entry(frm)
    courdescEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Courier type:",padding=10).grid(column=0, row=2)
    courtypeEtr = Entry(frm)
    courtypeEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="customer Id:",padding=10).grid(column=0, row=3)
    cusidEtr = Entry(frm)
    cusidEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="shipment Id:",padding=10).grid(column=0, row=4)
    shipidEtr = Entry(frm)
    shipidEtr.grid(column = 1, row = 4)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=9)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=9)

    window.mainloop()

# Add Shipment
def addShip():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(shipidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Supplier ID cannot be Empty')
        else:
            shipid = shipidEtr.get()
        if(fromcityEtr.get() == ''):
            fromcity = ''
        else:
            fromcity = fromcityEtr.get()
        if(tocityEtr.get() == ''):
            tocity = ''
        else:
            tocity = tocityEtr.get()
        if(offIdEtr.get() == ''):
            offId = ''
        else:
            offId = offIdEtr.get()
        

        addData.addshipment(shipid, fromcity, tocity, offId )

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    window.winfo_screenwidth()
    window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New shipment place")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Shipment ID:",padding=10).grid(column=0, row=0)
    shipidEtr = Entry(frm)
    shipidEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="from city:",padding=10).grid(column=0, row=1)
    fromcityEtr = Entry(frm)
    fromcityEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="to city:",padding=10).grid(column=0, row=2)
    tocityEtr = Entry(frm)
    tocityEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="office Id:",padding=10).grid(column=0, row=3)
    offIdEtr = Entry(frm)
    offIdEtr.grid(column = 1, row = 3)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)


    window.mainloop()