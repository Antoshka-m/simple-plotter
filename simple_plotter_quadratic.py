import tkinter as Tk
from tkinter.messagebox import showerror
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def check_if_float(var):
    try:
        float(var)
        return True
    except ValueError:
        return False
    
    
def plotting_tk(a, b, c):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    x = np.linspace(-10,10,100)
    plt.plot([x for x in x], [a*(x**2)+b*x+c for x in x], label = r'$Y = '+str(a)+r'x^2'+' + '+str(b)+'x'+' + '+str(c)+'$')
    plt.xlabel("X", fontsize=20)
    plt.ylabel("Y", fontsize=20)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xticks(fontsize = 14) 
    plt.yticks(fontsize = 14) 
    plt.tight_layout()
    plt.legend()
    plt.grid()
    canvas.show()
    plot_widget.grid(row=5, column = 0, columnspan=3)


def get_value():
    if not check_if_float(myvar.get()) or not check_if_float(myvar2.get()) or not check_if_float(myvar3.get()):
        print("Invalid entry. Enter integer or decimal numbers, please\n")
        showerror(title = "Error", message = "Invalid entry. Enter integer or decimal numbers, please")
        return None
    a=float(myvar.get())
    b=float(myvar2.get())
    c=float(myvar3.get())
    plotting_tk(a, b, c)

root = Tk.Tk()
myvar = Tk.StringVar()
myvar2= Tk.StringVar()
myvar3= Tk.StringVar()
l = Tk.Text(root, width=80, height=2, borderwidth=0)
l.tag_configure("subscript", offset=+4)
l.insert("insert", "Input coefficients for y = ax", "", "2", "subscript", " + bx + c")
l.config(font=(None, 15), state="disabled")
l.grid(row=0, column = 0, columnspan=2)
L_a = Tk.Label(master=root, text="a")
L_a.grid(row=1, column = 0)
L_a.config(font=(None, 15))
E_a = Tk.Entry(master=root, bd =2, textvariable=myvar)
E_a.grid(row=1, column = 1)
L_b = Tk.Label(master=root, text="b")
L_b.grid(row=2, column = 0)
L_b.config(font="TimesNewRoman 15")
E_b = Tk.Entry(master=root, bd =2, textvariable=myvar2)
E_b.grid(row=2, column = 1)
L_c = Tk.Label(master=root, text="c")
L_c.grid(row=3, column = 0)
L_c.config(font=(None, 15))
E_c = Tk.Entry(master=root, bd =2, textvariable=myvar3)
E_c.grid(row=3, column = 1)
button_get = Tk.Button(master=root, text='Plot!', command=get_value)
button_get.grid(row=4)
Tk.mainloop()

