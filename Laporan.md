## <center> **Laporan Mingguan Praktikum Metode Komputasi** <center>
### <center> Kelompok 1: <center>
#### <center> 1. Aulia Rizqikha <center>
#### <center> 2. Iha Sakti <center>
#### <center> 3. Isma Afrianti <center>
#### <center> 4. Muhammad Raffli <center>
#### <center> 5. Olivia Salma <center>
#### <center> 6. Riva Adhista <center>
#### <center> 7. Zahra Adinda <center>


**-----------------------------------------------------------------------------------------------------------------**
### <center> Minggu Pertama <center>


##### Pada minggu pertama ini, praktikkan diminta untuk membuat core program dari masing-masing masalah yang diminta. Untuk kelompok 1, masalah yang harus diselesaikan berupa tekanan hidrostatis pada tangki bocor. Berikut modul yang dibuat oleh kelompok kami:

import turtle

def hdr(r,g,h,hmax):
    """Menghitung Tekanan hidrostatis (massa jenis zat cair,gravitasi,kedalaman bocor (meter),tinggi tabung asli (meter) ) """
    t=turtle.Turtle()
    t.penup()
    t.goto(-100,-50)
    t.pendown()
    hdr = r*h*g
    z= hmax-h
    
     
    
    h2 = 200*(h1/(h1+z1))
    z2 = 200*(z1/(h1+z1))
        
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
    t.goto(-100,-70)
    t.write("Tekanan Hidrosatis :"+ str(hdr) + "N/m^2")
    
    turtle.done()
    turtle.mainloop()

def hidrostatis(r,g,h,hmax):
    if h > hmax:
        print('masukan nilai yang benar')
    else:
        hdr(r,g,h,hmax)


##### Untuk modul ini kami menggunakan library turtle untuk menggambar garis, lingkaran, dan bentuk lainnya yang lebih kompleks. Library ini akan digunakan untuk menggambar tabung bocor dalam 2 dimensi. Di sini kami mendefinisikan fungsi hidrostatis dengan parameter yang diinput, diantaranya massa jenis cairan (dilambangkan dengan r), gravitasi planet (dilambangkan dengan g), tinggi tabung dari atas permukaan (dilambangkan dengan h), dan tinggi tabung keseluruhan (dilambangkan dengan hmax).

##### Setelah menginput parameter tersebut, barulah masuk ke dalam proses perhitungan tekanan hidrostatis dan pembuatan gambar dengan library turtle. Untuk memunculkan kepala tanda panah, kami menggunakan fungsi "turtle.Turtle()". Kemudian, terdapat fungsi penup dan pendown, dimana fungsi penup digunakan untuk menghilangkan tinta warna pada garis yang dibuat dan fungsi pendown digunakan untuk menampilkan tinta warna pada garis yang dibuat. 

##### Kami memulai titik pada koordinat x=-100 dan y=-50. Pada code di atas terdapat variabel z, dimana variabel z merupakan tinggi dari titik bocor ke batas bawah tabung yang didapatkan dengan mengurangi nilai hmax dan h. Saat membuat gambarnya, terdapat fungsi forward(untuk maju), left(untuk ke kiri), dan right(untuk ke kanan) untuk membantu dalam pembuatannya. Fungsi forward menggunakan parameter jarak sehingga garis bergerak maju ke depan sesuai dengan jarak yang diminta. Sedangkan, fungsi left dan right menggunakan parameter sudut sehingga dapat bergerak belok sesuai dengan arah sudut yang diinginkan


**------------------------------------------------------------------------------------------------------------------**
### <center> Minggu Kedua <center>


#### Pada minggu kedua, kelompok kami melakukan sedikit perubahan pada modul hidrostatis yang sudah dibuat minggu lalu. Perubahan yang terjadi terdapat di window yang digunakan saat berjalannya program ini. Saat ini, kami menggunakan window tkinter karena saat program selesai dijalankan program tersebut tidak crash. Berikut modul terbaru setelah direvisi:

import tkinter as tk
import turtle

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
    
        """Menghitung Tekanan hidrostatis (massa jenis zat cair,gravitasi,kedalaman bocor (meter),tinggi tabung asli (meter) ) """
        t.penup()
        t.goto(-100,-150)
        t.pendown()
        hdr = r*h*g
        z= hmax-h
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
    

    t = turtle.RawTurtle(canvas)
    bool(rho,ge,ha,haem)
    t.hideturtle()
    root.mainloop()


#### Selain itu, kami juga melakukan optimasi terhadap program ini dengan menggunakan parallel processing karena untuk prosesnya sendiri lebih simple. Untuk mengoptimasi program ini kami menulis code seperti berikut:

from hidrostatis import hidrostatis
%timeit hidrostatis

#### Kami mengambil fungsi hidrostatis dari modul hidrostatis yang sudah dibuat. Timeit berfungsi untuk menghitung waktu dalam menjalankan program ini. Kemudian, dilanjutkan dengan menulis fungsi yang akan diukur kecepatannya saat menjalankan program. Program ini sudah optimal dengan menghabiskan waktu 21 ns.