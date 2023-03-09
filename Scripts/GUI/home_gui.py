from tkinter import *


window = Tk()
window.geometry("960x540")
window.title("CMS")

# GUI Logic.
outlinerFrame = Frame(window, bg="#535c5c", borderwidth=1,relief=SUNKEN)
outlinerFrame.pack(side=LEFT, fill="y")

topFrame = Frame(window, bg="white", border=4)
topFrame.pack(side=TOP, fill="x")

terminalFrame = Frame(window, bg="white", border=4,)
terminalFrame.pack(side=BOTTOM, fill= "x")

centerFrame = Frame(window, bg="white", border=4,)
centerFrame.pack(side=RIGHT, fill= "both")

# To display text in outliner.
# outlinerTexr = Label(outlinerFrame, text="Outliner...")
home_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Home")
home_button.pack(pady=10, padx=50)

borrowers_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Borrowers")
borrowers_button.pack(pady=10,padx=50)

loans_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Loans")
loans_button.pack(pady=10,  padx=50)

payments_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Payments")
payments_button.pack(pady=10,  padx=50)


# To show display widgets in top window.
# fileHeading = Label(topFrame, text="File.txt")
fileHeading = Label(topFrame,bg = "white")
fileHeading.pack()


# To display widgets in bottom frame.
# terminalText = Label(terminalFrame, text="This is Your output window.")
terminalText = Label(terminalFrame, bg="white")
terminalText.pack(pady=50)



# TO DISPLAY WIDGETS IN CENTER centerFrame.
Payments_button = Button(centerFrame,height=2,width=20,fg="white",bg="#0694bc" ,text="View Payments")
Payments_button.pack(pady=50,  padx=40 , side=LEFT)

Borrowers_button = Button(centerFrame,height=2,width=20,fg="white",bg="#0c9c3a" ,text="View Borrowers")
Borrowers_button.pack(pady=50,  padx=40 , side=LEFT)

Loans_button = Button(centerFrame,height=2,width=20,fg="white",bg="#8221c4", text="View Loans")
Loans_button.pack(pady=50,  padx=40 , side=LEFT)
window.mainloop()