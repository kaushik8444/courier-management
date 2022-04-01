from tkinter import *
from tkinter import ttk
import addNew
import viewAll


def win():
   # window creation
    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("express delivery")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Employee
    empRow = 0
    ttk.Label(frm,text="Employee",padding=10).grid(column=0,row=empRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=empRow)

    addEmpBtn = ttk.Button(frm, text="Add New", command=addNew.addEmp)
    addEmpBtn.grid(column=2,row=empRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=empRow)
    
    viewAllEmpBtn = ttk.Button(frm, text="View All", command=viewAll.viewEmp)
    viewAllEmpBtn.grid(column=4,row=empRow)

    # office
    offRow = 1
    ttk.Label(frm,text="Office",padding=10).grid(column=0,row=offRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=offRow)

    addoffBtn = ttk.Button(frm, text="Add New", command=addNew.addOff)
    addoffBtn.grid(column=2,row=offRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=offRow)
    
    viewAlloffBtn = ttk.Button(frm, text="View All", command=viewAll.viewOff)
    viewAlloffBtn.grid(column=4,row=offRow)

    # Customer
    cusRow = 2
    ttk.Label(frm,text="Customer",padding=10).grid(column=0,row=cusRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=cusRow)

    addEmpBtn = ttk.Button(frm, text="Add New", command=addNew.addCus)
    addEmpBtn.grid(column=2,row=cusRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=cusRow)
    
    viewAllEmpBtn = ttk.Button(frm, text="View All", command=viewAll.viewCus)
    viewAllEmpBtn.grid(column=4,row=cusRow)

    # courier
    courRow = 3
    ttk.Label(frm,text="Courier",padding=10).grid(column=0,row=courRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=courRow)

    addcourBtn = ttk.Button(frm, text="Add New", command=addNew.addCour)
    addcourBtn.grid(column=2,row=courRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=courRow)
    
    viewAllcourBtn = ttk.Button(frm, text="View All", command=viewAll.viewCou)
    viewAllcourBtn.grid(column=4,row=courRow)

    # shipment
    shipRow = 4
    ttk.Label(frm,text="Shipment",padding=10).grid(column=0,row=shipRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=shipRow)

    addshipBtn = ttk.Button(frm, text="Add New", command=addNew.addShip)
    addshipBtn.grid(column=2,row=shipRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=shipRow)
    
    viewAllshipBtn = ttk.Button(frm, text="View All", command=viewAll.viewShip)
    viewAllshipBtn.grid(column=4,row=shipRow)

    ttk.Button(frm, text="check Out", command=window.destroy).grid(column=2,row=5)

    window.mainloop()