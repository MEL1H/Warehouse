parcano="#ParcaNo#"

import tkinter as tk

width=1024
height=768
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
msgbox.pack()
content.pack()
window.mainloop()