parcano="#ParcaNo#"

import tkinter as tk

width=800
height=600
window=tk.Tk()
window.wm_attributes("-fullscreen","off")
screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
halfheight=screenheight/2
halfwidth=screenwidth/2
locx=halfwidth-width/2
locy=halfheight-height/2
window.geometry("%dx%d+%d+%d" %(width,height,locx,locy))
window.title("{parcano} BALANS KESİM PROGRAMI".format(parcano=parcano))
content=tk.Label(text="WELCOME",
width=int(width/2),
height=int(height/2))
content.pack()
window.mainloop()