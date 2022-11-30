from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
from hidrostatis import hidrostatis


root = Tk()
root.geometry("400x150")

labelfr = LabelFrame(root,text="result",padx=20,pady=20)
labelfr.place(x=60,y=380)

x = Label(root,text = "Masukan rho")
g= Label(root,text = "Gaya Gravitasi")
h = Label(root,text = " Masukan\n kedalaman bocor\n(dalam meter)")
m=  Label(root,text = "kedalaman asli\ntabung")
e1 = Entry(root,width=10)
e2 = Entry(root,width=10)
e3 = Entry(root,width=10)
e4 = Entry(root,width=10)
x.place(x = 16, y = 50)
e1.place(x = 20, y = 70)
g.place(x = 113, y = 50)
e2.place(x = 120, y = 70)
h.place(x = 202, y = 20)
e3.place(x = 220, y = 70)
m.place(x = 310, y = 30)
e4.place(x = 320, y = 70)
def plot():
    r=float(e1.get())
    g=float(e2.get())
    h=float(e3.get())
    m=float(e4.get())
    hidrostatis(r,g,h,m)
   


root.title(' Mencari Tekanan Hidrostatis Dalam Tangki Bocor ')
plot_button = Button(master = root, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Proses")
plot_button.place(x = 160, y = 100)
root.mainloop()
