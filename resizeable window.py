from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
f1 = Frame(root, bg="grey", borderwidth=6, relief = SUNKEN)
f1.pack(side=LEFT, fill='y')
#pack options - anchor =nw, side= top, bottom, left, right fill  padx pady
l = Label(f1, text = "Project")
l.pack(pady=142)
l.pack(side=BOTTOM, anchor="sw", fill = X)

root.mainloop()