from tkinter import *
import ledger_bk
window = Tk()
window.title("Account Ledger")

def view_command():
    lb.delete(0,END)
    for row in ledger_bk.viewall():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in ledger_bk.search(name=name.get(),user=user.get(),password=password.get(),category=category.get()):
        lb.insert(END,row)

def add_command():
    ledger_bk.add(name.get(),user.get(),password.get(),category.get(),cdate.get())
    lb.delete(0,END)
    lb.insert(END,name.get(),user.get(),password.get(),category.get(),cdate.get())

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

def update_command():
    ledger_bk.update(selected_tuple[0],name.get(),user.get(),password.get(),category.get(),cdate.get())
    view_command()

def delete_command():
    ledger_bk.delete(selected_tuple[0])
    view_command()
    #lb.delete(END,get_selected_row.selected_tuple)
def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
