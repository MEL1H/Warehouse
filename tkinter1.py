import tkinter as tk

window=tk.Tk()
window.geometry("400x400")
window.wm_attributes("-fullscreen","off")
button=tk.Button(
text="click me",
width="25",
height="5",
bg="green",
fg="yellow",
)
button.pack()
window.mainloop()