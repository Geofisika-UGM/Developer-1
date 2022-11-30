import tkinter as tk
import turtle
import threading
def hidrostatis(rho,ge,ha,haem):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=600)
    canvas.pack()
    
    def bool(r,g,h,hmax):
        if h > hmax:
            print('masukan nilai yang benar')
        else:
            hdr(r,g,h,hmax)
        
    def hdr(r,g,h,hmax):
        t = turtle.RawTurtle(canvas)
        """Menghitung Tekanan hidrostatis (massa jenis zat cair,gravitasi,kedalaman bocor (meter),tinggi tabung asli (meter) ) """
        t.penup()
        t.goto(-100,-150)
        t.pendown()
        hdr = r*h*g
        z= hmax-h
        v=(2*g*z)**0.5
        h2 = 300*(h/(h+z))
        z2 = 300*(z/(h+z))
        x=6
        t.pensize(2)
        t.pencolor('black')
        t.fillcolor('cyan')
        t.begin_fill()
        t.forward((h2+x+z2)/2)
        t.left(90)
        t.forward(z2/2)
        t.write(" "+ str(z) + "m")
        t.forward(z2/2)
        t.right(90)
        t.forward(x)
        t.penup()
        for i in range(90):
            t.forward(1)
            t.right(1)
        t.forward(1)
        t.forward(z2/2)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(z2/2)
        t.forward(x)
        for i in range(90):
            t.forward(1)
            t.left(1)
        t.forward(1)
        t.forward(x)
        t.pendown()
        t.forward(x)
        t.right(90)
        t.forward(h2/2)
        t.write(" "+ str(h) + "m")
        t.forward(h2/2)
        t.left(90)
        t.penup()
        t.forward((h2+x+z2)/2)
        t.left(90)
        t.pendown()
        t.forward((h2+x+z2)/2)
        t.write(" "+ str(h+z) + "m")
        t.forward((h2+x+z2)/2)
        t.end_fill()
        t.penup()
        t.goto(-100,-170)
        t.write("Tekanan Hidrosatis :"+ str(hdr) + "N/m^2")
        t.hideturtle()
    t1 = threading.Thread(target=bool, args=(rho,ge,ha,haem))
    t1.start()
    root.mainloop()