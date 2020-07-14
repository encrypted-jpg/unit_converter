
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from scales import get_scale_factor, scale_temp
import tkinter.messagebox as messagebox

root = Tk()
root.title("Unit Converter")
root.geometry("500x200")
Label(root, text = "Select a Tab").grid(row = 0, column = 0, columnspan = 3)

def add_menu(root):
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    helpmenu = Menu(menu)
    menu.add_cascade(label="File", menu = filemenu)
    filemenu.add_command(label = "Exit", command = root.quit)
    menu.add_cascade(label="Help", menu = helpmenu)
    helpmenu.add_command(label="About", command = about)

def about():
    co = "© Aditya V\nVersion 0.1"
    abc = "This will show you the result after the conversion..\n" + co
    messagebox.showinfo("About", "This is an unit converter..\nSelect a tab..\nEnter the floating or integer value \nand then click on convert..\n"+ abc)

def add_tabs(root):
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Length")
    tabControl.add(tab2, text="Area")
    tabControl.add(tab3, text="Temperature")
    tabControl.grid(row=1, column=0)
    # ttk.Label(tab1, text="HI").grid(row=0, column=1)
    # ttk.Label(tab2, text="HI it's me").grid(row=0, column=1)
    length(tab1)
    area(tab2)
    temperature(tab3)


def length(tab):
    ttk.Label(tab, text = "        ").grid(row = 0, column = 0)
    ttk.Label(tab, text="Enter Here: ").grid(row = 1, column=0)
    ent = Entry(tab)
    ent.grid(row = 1, column = 1)
    ttk.Label(tab, text="        ").grid(row=2, column=0)
    ent_chosen = ttk.Combobox(tab, width = 10, textvariable=StringVar())
    ent_chosen['values'] = ("Nanometers", "Microns", "Millimeters", "Centimeters", "Meters", "Kilometers", "Inches","Feets","Yards", "Miles")
    ent_chosen.grid(row = 3, column = 0, columnspan = 2)
    ent_chosen.current(4)
    to_chosen = ttk.Combobox(tab, width=10, textvariable=StringVar())
    to_chosen['values'] = ("Nanometers", "Microns", "Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feets", "Yards", "Miles")
    to_chosen.grid(row=3, column=3, columnspan=2)
    to_chosen.current(4)
    ttk.Label(tab, text="        ").grid(row=4, column=0)
    convert = Button(tab, text ="Convert", font = tkFont.Font(size=10), width = 15, command = lambda : conv_length(tab, ent, ent_chosen, to_chosen))
    convert.grid(row = 5, column = 1, columnspan = 3)
    ttk.Label(tab, text="Result = ").grid(row=1, column=4, columnspan=2)

def conv_length(tab, ent, ent_chosen, to_chosen):
    values_list = ["Nanometers", "Microns", "Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feets", "Yards", "Miles"]
    entr = ent_chosen.get()
    cha = to_chosen.get()
    try:
        user = float(ent.get())
        scale_factor = get_scale_factor("length", values_list.index(entr), values_list.index(cha))
        ttk.Label(tab, text="                                          ").grid(row=1, column=7)
        ttk.Label(tab, text = str(float(scale_factor*user))+"  ").grid(row = 1, column = 7)
    except:
        messagebox.showinfo("Invalid Input!!", "Please Give a valid input...")

def area(tab):
    ttk.Label(tab, text = "        ").grid(row = 0, column = 0)
    ttk.Label(tab, text="Enter Here: ").grid(row = 1, column=0)
    ent = Entry(tab)
    ent.grid(row = 1, column = 1)
    ttk.Label(tab, text="        ").grid(row=2, column=0)
    ent_chosen = ttk.Combobox(tab, width = 20, textvariable=StringVar())
    ent_chosen['values'] = ("Square Millimeters", "Square Centimeters", "Square Meters", "Hectares", "Square Kilometers",
                            "Square Inches","Square Feet","Square Yards", "Acres", "Square Miles")
    ent_chosen.grid(row = 3, column = 0, columnspan = 2)
    ent_chosen.current(2)
    to_chosen = ttk.Combobox(tab, width=20, textvariable=StringVar())
    to_chosen['values'] = ("Square Millimeters", "Square Centimeters", "Square Meters", "Hectares", "Square Kilometers",
                           "Square Inches","Square Feet","Square Yards", "Acres", "Square Miles")
    to_chosen.grid(row=3, column=3, columnspan=2)
    to_chosen.current(2)
    ttk.Label(tab, text="        ").grid(row=4, column=0)
    convert = Button(tab, text ="Convert", font = tkFont.Font(size=10), width = 15, command = lambda : conv_area(tab, ent, ent_chosen, to_chosen))
    convert.grid(row = 5, column = 1, columnspan = 3)
    ttk.Label(tab, text="Result = ").grid(row=1, column=4, columnspan=2)

def conv_area(tab, ent, ent_chosen, to_chosen):
    values_list = ["Square Millimeters", "Square Centimeters", "Square Meters", "Hectares", "Square Kilometers",
                   "Square Inches","Square Feet","Square Yards", "Acres", "Square Miles"]
    entr = ent_chosen.get()
    cha = to_chosen.get()
    try:
        user = float(ent.get())
        scale_factor = get_scale_factor("area", values_list.index(entr), values_list.index(cha))
        ttk.Label(tab, text="                                          ").grid(row=1, column=7)
        ttk.Label(tab, text = str(float(scale_factor*user))+"  ").grid(row = 1, column = 7)
    except:
        messagebox.showinfo("Invalid Input!!", "Please Give a valid input...")

def temperature(tab):
    ttk.Label(tab, text = "        ").grid(row = 0, column = 0)
    ttk.Label(tab, text="Enter Here: ").grid(row = 1, column=0)
    ent = Entry(tab)
    ent.grid(row = 1, column = 1)
    ttk.Label(tab, text="        ").grid(row=2, column=0)
    ent_chosen = ttk.Combobox(tab, width = 15, textvariable=StringVar())
    ent_chosen['values'] = ("Celsius", "Fahrenheit", "Kelvin")
    ent_chosen.grid(row = 3, column = 0, columnspan = 2)
    ent_chosen.current(2)
    to_chosen = ttk.Combobox(tab, width=15, textvariable=StringVar())
    to_chosen['values'] = ("Celsius", "Fahrenheit", "Kelvin")
    to_chosen.grid(row=3, column=3, columnspan=2)
    to_chosen.current(2)
    ttk.Label(tab, text="        ").grid(row=4, column=0)
    convert = Button(tab, text ="Convert", font = tkFont.Font(size=10), width = 15, command = lambda : conv_temp(tab, ent, ent_chosen, to_chosen))
    convert.grid(row = 5, column = 1, columnspan = 3)
    ttk.Label(tab, text="Result = ").grid(row=1, column=4, columnspan=2)

def conv_temp(tab, ent, ent_chosen, to_chosen):
    values_list = ["Celsius", "Fahrenheit", "Kelvin"]
    entr = ent_chosen.get()
    cha = to_chosen.get()
    try:
        user = float(ent.get())
        values = scale_temp(values_list.index(entr), values_list.index(cha), user)
        ttk.Label(tab, text="                                          ").grid(row=1, column=7)
        ttk.Label(tab, text = str(values) + "  ").grid(row = 1, column = 7)
    except:
        messagebox.showinfo("Invalid Input!!", "Please Give a valid input...")

add_menu(root)
add_tabs(root)
root.mainloop()

