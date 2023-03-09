from tkinter import * 
from tkhtmlview import *

import sys
import os
sys.path.append(os.path.abspath("./XL editor"))
import caller

window = Tk()

window.title(" C. M. S.")

window.geometry("960x540")

details_String = ["loan Id","First Name","Last Name","Mobile Number","Address","Aadhaar Number","Pan Number","Bank Name","Account Number","Amount","Commision To","Commission in Percentage","Commision in Rupees"]

def getData():
    global newlabel,details_String
    
    s = ""
    myListOfValues = caller.getData(tempLoanStr.get())
    # for a in range(0, len(myListOfValues)):
    #     s += details_String[a] + " : " + str(myListOfValues[a]) + "\n"

    for i in range(13):
        for j in range(1,3):

            e = Entry(relief = GROOVE)

            e.grid(row=i, column=j, sticky=NSEW)

            if j==1:
                e.insert(END,details_String[i])
            else:
                e.insert(END,myListOfValues[i])

    # TempLoanId.pack_forget()
    # newlabel.config(text= s) 


# newlabel = Label(text = " Our Journey Starts Here.....")
# newlabel.grid(row=0,column=0)
# tempLoanStr = StringVar()
# TempLoanId = Entry(window, bd = 5, textvariable=tempLoanStr)
# TempLoanId.grid(row=1, column=0)



# btn = Button(window,text="Get data", command=getData)

# btn.grid(row=2,column=0)

HTMLLabel(window, html= '<a href="https://www.google.com">Continue</a>').pack()
# HTMLLabel(window, html = '<button type="button">Close</button>').pack()


window.mainloop()
