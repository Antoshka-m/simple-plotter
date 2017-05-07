import tkinter as Tk
from tkinter.messagebox import showerror
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import numpy as np

def close_all():
    root.quit()
    root.destroy()
    

def check_if_float(var):
    try:
        float(var)
        return True
    except ValueError:
        return False
    
    
def plotting_tk(a, b, c):   #plotting quadratic function with given coefficients
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root) #embedding canvas with plot
    canvas.show()
    plot_widget = canvas.get_tk_widget()
    x = np.linspace(-10,10,100)
    plt.plot([x for x in x], [a*(x**2)+b*x+c for x in x], label = r'$Y = '+str(a)+r'x^2'+' + '+str(b)+'x'+' + '+str(c)+'$')
    plt.xlabel("X", fontsize=20)
    plt.ylabel("Y", fontsize=20)
    plt.xticks(fontsize = 14) 
    plt.yticks(fontsize = 14) 
    plt.tight_layout()
    plt.legend()
    plt.grid()
    plot_widget.grid(row=0, column = 3, columnspan=3, rowspan=4) #placing canvas 
    toolbar_frame = Tk.Frame(root) #toolbar as separate frame to avoid conflict between grid and pack. (Navigation toolbar has paack already)
    toolbar_frame = NavigationToolbar2TkAgg(canvas, root) 
    toolbar_frame.update()
    toolbar_frame.grid(row=5, column=3) #placing 

    
def get_values(): #getting coefficient values from entry forms and execution plotting function
    if not check_if_float(var_a.get()) or not check_if_float(var_b.get()) or not check_if_float(var_c.get()):
        showerror(title = "Error", message = "Invalid entry. Enter integer or decimal numbers, please")
        return None
    a=float(var_a.get())
    b=float(var_b.get())
    c=float(var_c.get())
    plotting_tk(a, b, c)


root=Tk.Tk() #initialize tkinter
root.protocol('WM_DELETE_WINDOW', close_all)  
var_a = Tk.StringVar(root)
var_b= Tk.StringVar(root)
var_c= Tk.StringVar(root)
l_text = Tk.Text(root, width=40, height=2, borderwidth=0)
l_text.tag_configure("subscript", offset=+4)
l_text.insert("insert", "Input coefficients for y = ax", "", "2", "subscript", " + bx + c")
l_text.config(font=(None, 15), state="disabled")
l_text.grid(row=0, column = 0, columnspan=2)
l_a = Tk.Label(master=root, width=5, height=2, bd =2, text="a", anchor="e") # a label
l_a.grid(row=1, column = 0)
l_a.config(font=(None, 15))
e_a = Tk.Entry(master=root, width=10, bd =2, textvariable=var_a) # a entry field
e_a.grid(row=1, column = 1)
e_a.config(font=(None, 15))
l_b = Tk.Label(master=root, width=5, height=2, bd =2, text="b", anchor="e") # b label
l_b.grid(row=2, column = 0)
l_b.config(font=(None, 15))
e_b = Tk.Entry(master=root, width=10, bd =2, textvariable=var_b) # b entry field
e_b.grid(row=2, column = 1)
e_b.config(font=(None, 15))
l_c = Tk.Label(master=root, width=5, height=2, bd =2, text="c", anchor="e") # c label
l_c.grid(row=3, column = 0)
l_c.config(font=(None, 15))
e_c = Tk.Entry(master=root, width=10, bd =2, textvariable=var_c) # c entry field
e_c.grid(row=3, column = 1)
e_c.config(font=(None, 15))
L_empty = Tk.Label(master=root, text="")
L_empty.grid(row=4)
button_get = Tk.Button(master=root, text='Plot!', command=get_values) # plot button
button_get.config(font=(None, 15))
button_get.grid(row=5, column=0)
button_quit=Tk.Button(root, text="Quit", command=close_all) # quit button
button_quit.config(font=(None, 15))
button_quit.grid(row=0, column=2)
root.mainloop()
