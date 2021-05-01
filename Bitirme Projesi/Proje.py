
parcano="3333"

import tkinter as tk

window=tk.Tk()
window.wm_attributes("-fullscreen","off")
window.geometry("500x300")
window.title("{parcano} BALANS KESİM PROGRAMI".format(parcano=parcano))
content1=tk.Label(
	text="hosgeldin")
content1.pack()
window.mainloop()