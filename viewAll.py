from tkinter import *
from tkinter import ttk
import connect_exmp
import deleteData
import updateUi

def viewEmp():

    def btnDel():
        window.destroy()
        deleteData.delEmpUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateEmpDio()     

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Employee")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Employee ID:",padding=10,relief="sunken").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Employee Name:",padding=10,relief="sunken").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Phone no::",padding=10,relief="sunken").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Address:",padding=10,relief="sunken").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Office ID:",padding=10,relief="sunken").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)


    lst = connect_exmp.empLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=4, row=i+2)
    ttk.Label(frm, text="",padding=5).grid(column=17, row=i+1)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=6, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=8,row=i+2)

    window.mainloop()

def viewOff():

    def btnDel():
        window.destroy()
        deleteData.delOffUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateoffDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Office")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields

    ttk.Label(frm, text="Office ID:",padding=10,relief="sunken").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Office Name:",padding=10,relief="sunken").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Office Address:",padding=10,relief="sunken").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)

    lst = connect_exmp.offLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=0, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=i+1)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=2, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=4,row=i+2)

    window.mainloop()

def viewCus():

    def btnDel():
        window.destroy()
        deleteData.delCusUI() 

    def btnUpdate():
        window.destroy()
        updateUi.updateCusDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Customer")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Customer ID:",padding=10,relief="sunken").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Customer Name:",padding=10,relief="sunken").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Phone No:",padding=10,relief="sunken").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Mail:",padding=10,relief="sunken").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Address:",padding=10,relief="sunken").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)

    lst = connect_exmp.cusLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=4, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=6, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=8,row=i+2)

    window.mainloop()

def viewShip():

    def btnDel():
        window.destroy()
        deleteData.delShipUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateshipDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Shipment")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Shipment ID:",padding=10,relief="sunken").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="From City:",padding=10,relief="sunken").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="To City:",padding=10,relief="sunken").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Office Id:",padding=10,relief="sunken").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    lst = connect_exmp.shipLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=2, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=4, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=6,row=i+2)

    window.mainloop()

def viewCou():

    def btnDel():
        window.destroy()
        deleteData.delCouUI()

    def btnUpdate():
        window.destroy()
        updateUi.updatecourDio()


    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Courier")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Courier ID:",padding=10,relief="sunken").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Courier Description:",padding=10,relief="sunken").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Courier Type:",padding=10,relief="sunken").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Customer ID:",padding=10,relief="sunken").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Shipment ID:",padding=10,relief="sunken").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)

    lst = connect_exmp.courLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=4, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=6, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=8,row=i+2)

    window.mainloop()