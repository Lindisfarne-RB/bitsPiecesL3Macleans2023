from tkinter import *
from PIL import Image, ImageTk
#python -m pip install Pillow on the terminal


root = Tk()
root.title("Goal Tracker")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can deposit or withdraw  money and see your progress towards your goals.")
 
# Create the message label and add it to the window using pack()
message_label = Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

#Create a PhotoImage()
neutral_image = PhotoImage(file="Notes.png")

#Create a new Label using the PhotoImage and pack it into the GUI

image_label = Label(root, image =neutral_image)
image_label.pack()

# Run the main window loop
root.mainloop()
