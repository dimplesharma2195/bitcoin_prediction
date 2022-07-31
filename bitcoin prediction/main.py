from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import requests
import json

bgco = "black"
co2 = "#94B49F"
window = Tk()
window.title('bitcoin price tracker')
window.geometry('320x360')
window.configure(bg = bgco)

def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CINR%2CCAD"
    r=requests.get(api_link)
    dic= r.json()


    usd_value = float(dic["USD"])
    usd_formatted_value="${:,.3f}".format(usd_value)
    usd["text"] = usd_formatted_value


    euro_value = float(dic["EUR"])
    euro_formatted_value = "{:,.3f}".format(euro_value)
    euros["text"] = "Canada  : CAD " + euro_formatted_value

    
    cad_value = float(dic["CAD"])
    cad_formatted_value = "{:,.3f}".format(cad_value)
    cad["text"] = "Europe : € " + cad_formatted_value

    
    inr_value = float(dic["INR"])
    inr_formatted_value = "{:,.3f}".format(inr_value)
    inr["text"] = "India : INR " + inr_formatted_value

    frame_body.after(1000, info)

frame_head = Frame(window, width=320 , height=60 , bg="white")
frame_head.grid(row=1 , column=0)

frame_body = Frame(window, width=320 , height=300 , bg="green")
frame_body.grid(row=2 , column=0)

image_1 = Image.open('bitcoin.png')
image_1 = image_1.resize((40,40))
image_1 = ImageTk.PhotoImage(image_1)

icon_1 = Label(frame_head, image = image_1 , bg = "white")
icon_1.place(x=10 , y=10)

name = Label(frame_head, text="Bitcoin Price Tracker" , fg = co2 , bg = "white" ,  anchor="center" , width= 15 , height=2 , font=('Poppins 20'))
name.place(x=50 , y=5)

usd= Label(frame_body, text= "$0000", width=14, height=1, font=('Arial 12 bold'), bg=co2, fg=bgco, anchor="center")
usd.place(x=0, y=28)

euros=Label(frame_body, text= "$0000", height=1, font=('Arial 15 bold'), bg=co2, fg=bgco, anchor="center")
euros.place(x=10, y=130)

cad=Label(frame_body, text= "$0000", height=1, font=('Arial 15 bold'), bg=co2, fg=bgco, anchor="center")
cad.place(x=10, y=170)

inr=Label(frame_body, text= "$0000", height=1, font=('Arial 15 bold'), bg=co2, fg=bgco, anchor="center")
inr.place(x=10, y=210)



info()
window.mainloop()