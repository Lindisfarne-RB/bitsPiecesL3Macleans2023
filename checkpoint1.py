from tkinter import *
from tkinter import ttk

# Call name function
def printme():
    subscribed_name_message.set("Thank you " + str(name_address_value.get()) + "! You are subscribed to our newsletter.")
    print("Thank you " + str(name_address_value.get()) + "! You are subscribed to our newsletter.")

root = Tk()
root.title("Macleans Newsletter")
root.geometry("400x700")

# Title (why is it red)
message_text = StringVar()
message_text.set("\n WELCOME TO \n MACLEANS SCHOOL NAVIGATION APP")

message_label = Label(root, textvariable=message_text, wraplength=250, fg="darkred", font=("Arial", 9, "bold"), justify="center")
message_label.grid(row=0, column=0, columnspan=2, padx=75, pady=10)

# Macleans logo
macleans_logo_image = PhotoImage(file="Notes.png")
macleans_logo = ttk.Label(root, image=macleans_logo_image)
macleans_logo.grid(row=1, column=0, columnspan=2, padx=10, pady=30)

# Email address stuff
email_address_label = Label(root, text="Enter your email address", fg="blue", font=("Arial", 12))
email_address_label.grid(row=5, column=0, sticky="W")

email_address_value = StringVar()
email_address_value.set("")

email_address_input = ttk.Entry(root, textvariable=email_address_value)
email_address_input.grid(row=6, column=0, padx=0, sticky="W")

# Name address stuff
name_address_label = Label(root, text="Enter your name", fg="blue", font=("Arial", 12))
name_address_label.grid(row=7, column=0, sticky="W")

name_address_value = StringVar()
name_address_value.set("")

name_address_input = ttk.Entry(root, textvariable=name_address_value)
name_address_input.grid(row=8, column=0, padx=0, sticky="W")

chosen_option = StringVar()

# Create a list of items for the Option Menu
options = ['Vanilla', 'Strawberry', 'Chocolate']

# Create the option menu and place in row 3, column 0
option_menu = ttk.OptionMenu(root, chosen_option, options[0], *options)
option_menu.grid(row=3, column=0, padx=10, pady=5)

# Submit button
submit_button = Button(root, text="Submit", command=printme, background="#fff2cc")
submit_button.grid(row=10, column=0, padx=0, pady=10, sticky="W")

# Thank you message
subscribed_name_message = StringVar()
subscribed_name_message.set("")

thank_you_label = Label(root, textvariable=subscribed_name_message, fg="blue", font=("Arial", 12))
thank_you_label.grid(row=11, column=0, pady=20, sticky="NSEW")

# Macleans logo (again) got help online on how to resize this because code avengers did not teach this
macleans_logo_botom_image = PhotoImage(file="Notes.png")
width = macleans_logo_botom_image.width()
height = macleans_logo_botom_image.height()

new_width = int(width / 4)
new_height = int(height / 4)

resized_image = macleans_logo_botom_image.subsample(int(width/new_width), int(height/new_height))

macleans_logo_botom = ttk.Label(root, image=resized_image)
macleans_logo_botom.grid(row=12, column=0, columnspan=2, padx=10, pady=30)

root.mainloop()
