from tkinter import *

layar= Tk()
layar.geometry("750x250")
layar.title ("kalkulator ")
layar.geometry("570x650+100+200")
layar.resizable(False,True)
layar.configure(bg="#46D3A0")
operator = ""


def Tampil(value):
    global operator
    
    operator+=value
    label_result.config(text=operator)

def bersikan_angka():
    global operator
    operator = ""
    label_result.config(text=operator)




def hitung():
    global operator
    result = ""
    if operator !="":
        try:
            result= eval(operator)
        except:
            result="error bro"
            operator= ""
    label_result.config(text=result)


label_result = Label(layar,width=25,height=2,text="",bg="#687cab",font=("arial",30))
label_result.pack()

Button(layar,text="c",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: bersikan_angka()).place(x=10,y=120)
Button(layar,text="/",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("/")).place(x=150,y=120)
Button(layar,text="%",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("%")).place(x=290,y=120)
Button(layar,text="*",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("*")).place(x=430,y=120)

Button(layar,text="9",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("9")).place(x=10,y=220)
Button(layar,text="8",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("8")).place(x=150,y=220)
Button(layar,text="7",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("7")).place(x=290,y=220)
Button(layar,text="6",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("6")).place(x=430,y=220)


Button(layar,text="5",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("5")).place(x=10,y=320)
Button(layar,text="4",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("4")).place(x=150,y=320)
Button(layar,text="3",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("3")).place(x=290,y=320)
Button(layar,text="2",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("2")).place(x=430,y=320)

Button(layar,text="1",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("1")).place(x=10,y=420)
Button(layar,text="0",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("0")).place(x=150,y=420)
Button(layar,text="**",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("**")).place(x=290,y=420)
Button(layar,text="=",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: hitung()).place(x=430,y=420)

Button(layar,text="-",width=5,border=0,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("-")).place(x=290,y=520)


Button(layar,text="+",width=5,height=1,font=("",30,"bold"),fg="black",bg="#AAEEEE",command=lambda: Tampil("+")).place(x=150,y=520)

layar.mainloop()