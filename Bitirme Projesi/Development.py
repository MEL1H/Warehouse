parcano="#ParcaNo#"
asd
import tkinter as tk

#version=m for mobile p for pc
ver="m2"


if ver=="p":	
	width=1366
	height=768
elif ver=="m":
	width=800
	height=600
else:
	raise ValueError("Versiyon duzelt")
		
window=tk.Tk()
window.resizable(0,0)
window.wm_attributes("-fullscreen","off")
screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
halfheight=screenheight/2
halfwidth=screenwidth/2
locx=halfwidth-width/2
locy=halfheight-height/2
window.geometry("%dx%d+%d+%d" %(width,height,locx,locy))
window.title("{parcano} BALANS KESİM PROGRAMI".format(parcano=parcano))

content=tk.Label(text="Bilgilendirme")
content.grid(row=1,column=1)
msgbox=tk.Text(window)
msgbox.grid(row=2,column=1)
msgbox.insert("3.0","deneme")
window.mainloop()
