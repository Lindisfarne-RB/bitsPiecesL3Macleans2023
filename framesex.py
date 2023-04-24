from tkinter import *
from tkinter import ttk
from tkinter import Tk


root = Tk()
root.title("Data input")


#Creating top frame
top_frame = LabelFrame(root, bg="red")
top_frame.grid(row=0, column=0, sticky="NSEW", pady=10,padx=10)


#Name label
name_label = ttk.Label(top_frame, text="Name:")
name_label.grid(padx=10, pady=10, sticky="NSEW")
#name input
name_entry = ttk.Entry(top_frame)
name_entry.grid(row=0, column=1, padx=10, pady=3)


#age Label
age_label = ttk.Label(top_frame, text="Age:")
age_label.grid(padx=10, pady=10, sticky="NSEW")
#age input
age_entry = ttk.Entry(top_frame)
age_entry.grid(row=1, column=1, padx=10, pady=3)


#House Label
house_label = ttk.Label(top_frame, text="House:")
house_label.grid(padx=10, pady=10, sticky="NSEW", column=2, row=1)
#House input
house_entry = ttk.Entry(top_frame)
house_entry.grid(row=1, column=3, padx=10, pady=3)


#Creating bottom frame
bottom_frame = LabelFrame(root, bg="blue")
bottom_frame.grid(row=1,column=0, sticky="NSEW", pady=10,padx=10)


#creating photo
image = PhotoImage(file="Notes.png")
image_label = ttk.Label(bottom_frame, image=image)
image_label.grid(row=0,column=0, pady=10,padx=10, rowspan=3)


#choice label
choice_label = ttk.Label(bottom_frame, text="Choice:")
choice_label.grid(column=1,row=0, pady=10, padx=10, sticky="N")


#choice combobox colors
choice_list = ['Red', 'Blue', 'Green', 'Pink']
chosen_choice = StringVar()
chosen_choice.set(choice_list[0])
choice_box = ttk.Combobox(bottom_frame, textvariable=choice_list, state="readonly")
choice_box['values'] = choice_list
choice_box.grid(column=2, row=0, pady=10, padx=10, sticky="N")


#submit button
submit_button = ttk.Button(bottom_frame, text="Submit")
submit_button.grid(row=1, column=1,pady=10, padx=10)


#Cancel button
cancel_button = ttk.Button(bottom_frame, text="Cancel")
cancel_button.grid(row=1, column=2,pady=10, padx=10)


#run mainloop
root.mainloop()

