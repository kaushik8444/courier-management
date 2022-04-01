from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import up
import updateData
import viewAll


# Update Employee
def updateEmpUi(id):
    def cancelBtn():
        window.destroy()
        viewAll.viewEmp()

    def updateBtn():
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
            offId = ''
        else:
            offId = offIdEtr.get()
         
        # print(empId + " " + empName + " " +empphone+ " " +empaddress + " " + offId )
        # print(type(salary))

        updateData.updateEmp(empId,empName,empphone,empaddress,offId)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewEmp()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Employee")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('employee', 'emp_id', id)

    # Fields
    ttk.Label(frm, text="Employee ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    empIdEtr = Entry(frm)
    empIdEtr.insert(0,str(lst[0]))
    # empIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Employee Name:",padding=10).grid(column=0, row=1)
    empNameEtr = Entry(frm)
    empNameEtr.insert(0,str(lst[1]))
    empNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Employee phone:",padding=10).grid(column=0, row=2)
    empphoneEtr = Entry(frm)
    empphoneEtr.insert(0,str(lst[2]))
    empphoneEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Employee address:",padding=10).grid(column=0, row=3)
    empaddressEtr = Entry(frm)
    empaddressEtr.insert(0,str(lst[3]))
    empaddressEtr.grid(column = 1, row = 3 )

    ttk.Label(frm, text="office Id:",padding=10).grid(column=0, row=4)
    offIdEtr = Entry(frm)
    offIdEtr.insert(0,str(lst[4]))
    offIdEtr.grid(column = 1, row = 4)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=8)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=8)

    window.mainloop()

# Update office
def updateOffUi(id):

    def CancelBtn():
        window.destroy()
        viewAll.viewOff()

    def updateBtn():

        if(offidEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Section No cannot be Empty')
        else:
            offId = offidEtr.get()
        
        if(offnameEtr.get() == ''):
            offname = ''
        else:
            offname = offnameEtr.get()
        
        if(offaddressEtr.get() == ''):
            offaddress = ''
        else:
            offaddress = offaddressEtr.get()

        updateData.updateoff(offId,offname,offaddress)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewOff()

    window = Tk()

    Width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Office")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('Office', 'off_Id', id)

    # Fields
    ttk.Label(frm, text="Office ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    offidEtr = Entry(frm)
    offidEtr.insert(0,str(lst[0]))
    #offidEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Office Name:",padding=10).grid(column=0, row=1)
    offnameEtr = Entry(frm)
    offnameEtr.insert(0,str(lst[1]))
    offnameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Office address:",padding=10).grid(column=0, row=2)
    offaddressEtr = Entry(frm)
    offaddressEtr.insert(0,str(lst[2]))
    offaddressEtr.grid(column = 1, row = 2)

    window.mainloop()

# Update Customer
def updateCusUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewCus()

    def updateBtn():

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

        updateData.updateCus(cusId, cusName, cusphone, cusemail, cusaddress)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewCus()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Customer")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('customer', 'cust_id', id)

    # Fields
    ttk.Label(frm, text="Customer ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    cusIdEtr = Entry(frm)
    cusIdEtr.insert(0,str(lst[0]))
    # cusIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Customer Name:",padding=10).grid(column=0, row=1)
    cusNameEtr = Entry(frm)
    cusNameEtr.insert(0,str(lst[1]))
    cusNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Customer phone:",padding=10).grid(column=0, row=2)
    cusphoneEtr = Entry(frm)
    cusphoneEtr.insert(0,str(lst[2]))
    cusphoneEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Customer email:",padding=10).grid(column=0, row=3)
    cusemailEtr = Entry(frm)
    cusemailEtr.insert(0,str(lst[3]))
    cusemailEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="customer address:",padding=10).grid(column=0, row=4)
    cusaddressEtr = Entry(frm)
    cusaddressEtr.insert(0,str(lst[4] ))
    cusaddressEtr.grid(column = 1, row = 4 )

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)

    window.mainloop()

# Update courier
def updatecourUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewCou()

    def updateBtn():
        if(courIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Supplier ID cannot be Empty')
        else:
            courId = courIdEtr.get()
        if(courdescEtr.get() == ''):
            courdesc = ''
        else:
            courdesc = courdescEtr.get()
        if(courtypeEtr.get() == ''):
            courtype = ''
        else:
            courtype = courtypeEtr.get()
        if(cusIdEtr.get() == ''):
            cusId = ''
        else:
            cusId = cusIdEtr.get()
        if(shipIdEtr.get() == ''):
            shipId = ''
        else:
            shipId = shipIdEtr.get()

        updateData.updatecour(courId, courdesc, courtype, cusId, shipId)

        messagebox.showinfo(title="Update",message="1 Row Updated")
        window.destroy()
        viewAll.viewCou()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update courier")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('courier', 'cour_id', id)

    # Fields
    ttk.Label(frm, text="courier ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    courIdEtr = Entry(frm)
    courIdEtr.insert(0,str(lst[0]))
    # courIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="courier description:",padding=10).grid(column=0, row=1)
    courdescEtr = Entry(frm)
    courdescEtr.insert(0,str(lst[1]))
    courdescEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="courier type:",padding=10).grid(column=0, row=2)
    courtypeEtr = Entry(frm)
    courtypeEtr.insert(0,str(lst[2]))
    courtypeEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="customer ID:",padding=10).grid(column=0, row=3)
    cusIdEtr = Entry(frm)
    cusIdEtr.insert(0,str(lst[3]))
    cusIdEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="shipment ID:",padding=10).grid(column=0, row=4)
    shipIdEtr = Entry(frm)
    shipIdEtr.insert(0,str(lst[4]))
    shipIdEtr.grid(column = 1, row = 4)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)


    window.mainloop()

# Update shipment
def updateshipUi(id):
    def cancelBtn():
        window.destroy()
        viewAll.viewShip()

    def updateBtn():
        if(shipIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
            shipId = shipIdEtr.get()
        if(fromcityEtr.get() == ''):
            fromcity = ''
        else:
            fromcity= fromcityEtr.get()
        if(tocityEtr.get() == ''):
            tocity = ''
        else:
            tocity = tocityEtr.get()
        if(offIdEtr.get() == ''):
            offId = ''
        else:
            offId = offIdEtr.get()
        
        updateData.updateship(shipId,fromcity,tocity,offId)

        messagebox.showinfo(title="Update",message="1 Row Updated")
        window.destroy()
        viewAll.viewShip()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Shipment")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('shipment', 'ship_Id', id)

    # Fields
    ttk.Label(frm, text="ship ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    shipIdEtr = Entry(frm)
    shipIdEtr.insert(0,str(lst[0]))
     # shipIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="from city:",padding=10).grid(column=0, row=1)
    fromcityEtr = Entry(frm)
    fromcityEtr.insert(0,str(lst[1]))
    fromcityEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="to city:",padding=10).grid(column=0, row=2)
    tocityEtr = Entry(frm)
    tocityEtr.insert(0,str(lst[2]))
    tocityEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="office ID:",padding=10).grid(column=0, row=3)
    offIdEtr = Entry(frm)
    offIdEtr.insert(0,str(lst[3]))
    offIdEtr.grid(column = 1, row = 3)    

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=9)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=9)

    window.mainloop()


# Dialog Boxes
def updateEmpDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('employee', 'emp_id' , id) != None):
                window.destroy()
                updateEmpUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewEmp()

    window = Tk()
    window.title("Update Employee")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Employee ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateoffDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('office', 'off_Id' , id) != None):
                window.destroy()
                updateOffUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewOff()

    window = Tk()
    window.title("Update office")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter office Id to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()


def updateCusDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('customer', 'cus_id' , id) != None):
                window.destroy()
                updateCusUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewCus()

    window = Tk()
    window.title("Update Customer")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Customer ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updatecourDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('Courier', 'Cour_id' , id) != None):
                window.destroy()
                updatecourUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewCou()

    window = Tk()
    window.title("Update Courier")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Courier ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateshipDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('shipment', 'ship_Id' , id) != None):
                window.destroy()
                updateshipUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewShip()

    window = Tk()
    window.title("update shipment")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter ship Id Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()
