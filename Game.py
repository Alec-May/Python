import tkinter

window = tkinter.Tk()
window.title("GUI")
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")
button1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack()
button2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()
button3 = tkinter.Button(bottom_frame, text = "Button3", fg = "purple").pack(side = "left")
button4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "left")

window.mainloop()

