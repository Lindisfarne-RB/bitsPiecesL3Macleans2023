'''use of checkbox in gui

from tkinter import *
root = Tk()
root.geometry("644x344")
root.mainloop()

'''

# first part id creating a form using a grid layout - second part is getting the info from form to a file
# this prog uses tkinter variable class - it has methods get and set
# grid is like excel row/column
from tkinter import *
root = Tk()
root.geometry("444x344")

def getvals():
      print("It works")
      print("Submitting form")
      print(f"{namevalue.get(), phonevalue.get() ,  gendervalue.get(),  emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get() }")

      with open("records.txt", "a") as f:
            f.write(f"{namevalue.get(), phonevalue.get() ,  gendervalue.get(),  emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get() }\n")
#heading goes here
Label(root, text="Welcome to ***ABC*** Travels" ,
      font = "comicsansms 17 bold", pady=15) .grid(row=0 , column = 3)
#text for form
name = Label (root, text="Name")
phone = Label (root, text="Phone")
gender = Label (root, text="Gender")
emergency = Label (root, text="Emergency Contact")
paymentmode  = Label (root, text="Payment Mode")

#packed text using grid
name.grid(row=1 , column=2)
phone.grid(row=2 , column=2)
gender.grid(row=3 , column=2)
emergency.grid(row=4 , column=2)
paymentmode.grid(row=5 , column=2)

#tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#entries for a form
#use cmd D to copy a full line
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

#packing the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)


#checkbox and packing it
foodservice = Checkbutton(text="Do you want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6,column=3)

#Button and packing it and assigning it a command

Button(text="Submit to Travels", command=getvals).grid(row=7,column=3)


#
root.mainloop()