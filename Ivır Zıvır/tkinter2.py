import tkinter as tk

window=tk.Tk()
window.wm_attributes("-fullscreen","off")
label=tk.Label(text="Hosgeldin")
entry=tk.Entry(fg="yellow",bg="green",width=10)
label.pack()
entry.insert(0,"python")
entry.pack()
window.mainloop()