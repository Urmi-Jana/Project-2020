from tkinter import *
import backend

def get_row(event):
    try:
        global sel_tuple
        index=list1.curselection()[0]
        sel_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,sel_tuple[1])
        e2.delete(0,END)
        e2.insert(END,sel_tuple[2])
        e3.delete(0,END)
        e3.insert(END,sel_tuple[3])
        e4.delete(0,END)
        e4.insert(END,sel_tuple[4])
    except IndexError:
        pass

def view_com():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_com():
    list1.delete(0,END)
    for row in backend.search(tit.get(), auth.get(),yr.get(),isb.get()):
        list1.insert(END,row)

def add_com():
    backend.insert(tit.get(), auth.get(),yr.get(),isb.get())
    list1.delete(0,END)
    list1.insert(END,(tit.get(), auth.get(),yr.get(),isb.get()))

def del_com():
    backend.delete(sel_tuple[0])

def update_com():
    backend.update(sel_tuple[0],tit.get(), auth.get(),yr.get(),isb.get())

wind=Tk()

wind.wm_title("BookStore App")


l1 = Label(wind, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(wind, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(wind, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(wind, text = "ISBN")
l4.grid(row = 1, column = 2)
 
tit=StringVar()
e1 = Entry(wind, textvariable=tit)
e1.grid(row=0, column=1)

auth=StringVar()
e2 = Entry(wind, textvariable=auth)
e2.grid(row=0, column=3)

yr=StringVar()
e3 = Entry(wind, textvariable=yr)
e3.grid(row=1, column=1)

isb=StringVar()
e4 = Entry(wind, textvariable=isb)
e4.grid(row=1, column=3)

list1=Listbox(wind, height= 6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(wind)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_row)

b1=Button(wind, text="View All", width=12, command=view_com)
b1.grid(row=2,column=3)

b2=Button(wind, text="Search Entry", width=12, command=search_com)
b2.grid(row=3,column=3)

b3=Button(wind, text="Add Entry", width=12, command=add_com)
b3.grid(row=4,column=3)

b4=Button(wind, text="Update selected", width=12, command=update_com)
b4.grid(row=5,column=3)

b5=Button(wind, text="Delete Selected", width=12,command=del_com)
b5.grid(row=6,column=3)

b6=Button(wind, text="Close", width=12, command=wind.destroy)
b6.grid(row=7,column=3)



wind.mainloop()