import cx_Oracle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connect_exmp
import viewAll
import updateData

def delData(tabName,idName,id):
    conn = cx_Oracle.connect('kaushik/8522@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('delete from {} where {} = {}'.format(tabName,idName,id))
    conn.commit()
    conn.close()

def delEmpUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('employee', 'emp_id' , id) != None):
                delData('employee', 'emp_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewEmp()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewEmp()

    window = Tk()
    window.title("Delete Employee")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Employee ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delOffUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('office', 'off_id' , id) != None):
                delData('office', 'off_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewOff()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewOff()

    window = Tk()
    window.title("Delete Office")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Office No to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delCusUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('customer', 'cus_id' , id) != None):
                delData('customer', 'cus_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewCus()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewCus()

    window = Tk()
    window.title("Delete Customer")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Customer ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delShipUI():
    
    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('shipment', 'ship_id' , id) != None):
                delData('shipment', 'ship_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewShip()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewShip()

    window = Tk()
    window.title("Delete shipment")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter shipment ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delCouUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('courier', 'cour_id' , id) != None):
                delData('courier', 'cour_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewCou()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewCou()

    window = Tk()
    window.title("Delete courier")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter courier No to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()
