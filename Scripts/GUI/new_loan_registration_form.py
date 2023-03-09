from tkinter import *
from datetime import date
from dateutil.relativedelta import relativedelta
from tkcalendar import DateEntry
import sys
import os



# ALL CUSTOM MADE SCRIPTS ARE IMPORTED BELOW.
sys.path.append(os.path.abspath("./XL editor"))
from idGenerator import *
from loanIdGenerator import *
from loanee_dataFinder import *
from loanee_dataEditor import *
from loan_dataEditor import *
from email_alert import *

window = Tk()
window.geometry("960x550")
window.configure(bg="white")
window.title("NEW LOANEE REGISTRATION")

# VARIABLES TO BE USED IN LOANEE REGISTRATION.
lID = StringVar()
amount_taken = IntVar()
interestPerc = StringVar()
timePeriod = IntVar()
payDay = StringVar()
startDay = StringVar()
endDay = StringVar()
emiAmount = IntVar()
totalAmount = StringVar()
commTo = StringVar()
comPer = StringVar()
comRup = StringVar()
totalEmi= timePeriod

ID = StringVar()

# METHOD TO CALL LOANEE_DATAEDITOR.PY AND REGISTER THE USER.
def register():
    ID = ID_Entry.get()
    amtTaken = amtTaken_Entry.get()
    IntPer = int(IntPer_Entry.get())
    timePeriod = TimePeriod_Entry.get("1.0","end-1c")
    PayDate = date(PayDate_Entry.get())
    ComTo = ComTo_Entry.get()
    ComPer = int(ComPer_Entry.get())

    # WE WILL GENERATE THE VALUE OF THE REMAINING VARAIBALES DYNAMICALLY.
    startDay = PayDate
    endDay = startDay + relativedelta(months = timePeriod)
    # TO GENERATE ID TO BE USED FOR TAKING LOANS.
    # ID = generateId(Name)
    lID = generateLoanId(ID)

    # MAIN ID WILL BE USED TO REGISTER THE LOANEE AND TO CREATE THE IDs FOR THE LOANS THAT HE TAKES.
    # lID = generateLoanId(ID)

    # TO REGISTER THE LOANEE FINALLY.
    detailWriter(lID,amount_taken,interestPerc,timePeriod,payDay,startDay,endDay,emiAmount,totalAmount,commTo,comPer,comRup,totalEmi)


    # A MESSAGE WILL BE SENT TO THE LOANEE FROM HERE THAT HE HAS SUCCESSFULLY REGISTERED WITH US.
    email_alert("Registeration Successfull",f'''
    Dear Loanee,
    Thanks for Choosing us.
    Here is Your {ID} which You can use to take loans.
    ''', email)




# -------------------------------GUI Logic.-------------------------------
outlinerFrame = Frame(window, bg="#535c5c", borderwidth=1,relief=SUNKEN)
outlinerFrame.pack(side=LEFT, fill="y")

LEFTFrame = Frame(window, bg="white", border=4)
LEFTFrame.pack(side=LEFT, fill="x")

terminalFrame = Frame(window, bg="white", border=4,)
terminalFrame.pack(side=BOTTOM, fill= "x")

centerFrame = Frame(window, bg="white", border=4,)
centerFrame.pack(fill= "both")

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


# To show display widgets in LEFT window.
# fileHeading = Label(LEFTFrame, text="File.txt")
fileHeading = Label(LEFTFrame,bg = "white")
fileHeading.pack()


# To display widgets in bottom frame.
# terminalText = Label(terminalFrame, text="This is Your output window.")
terminalText = Label(terminalFrame, bg="white")
terminalText.pack(pady=50)



# TO DISPLAY WIDGETS IN CENTER CENTERFRAME.

# LABELS IN CENTERFRAME.


# ---------------------WE ARE NOT GOING TO PUT THIS AS WE WILL OURSELF CREATE THE LOAN ID AND DISPLAY IT TO THE USER.---------------------
# loanId_label = Label(centerFrame, text="Loan Id",font="ariel 10 ", bg= "white", justify= LEFT).grid(row=1, column=1, padx=100, pady =5)

Id_label = Label(centerFrame, text="ID Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=2, column=1, padx=100, pady =5)

amtTaken_label = Label(centerFrame, text="Amount Taken",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=3, column=1, padx=100, pady =5)

IntPer_label = Label(centerFrame, text="Interest Percentage",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=4, column=1, padx=100, pady =5)

TimePeriod_label = Label(centerFrame, text="Time Period",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=5, column=1, padx=100, pady =5)

PayDate_label = Label(centerFrame, text="Pay Date",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=6, column=1, padx=100, pady =5)

ComTo_label = Label(centerFrame, text="Commision To",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=7, column=1, padx=100, pady =5)

ComPer_label = Label(centerFrame, text="Commision Percentage",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=8, column=1, padx=100, pady =5)

# AccountNumber_label = Label(centerFrame, text="Account Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=9, column=1, padx=100, pady =5)







# TEXT ENTRY WIDGETS IN CENTERFRAME.
# loanId_Entry = Entry(centerFrame, textvariable=lID).grid(row=1,column=2)
ID_Entry = Entry(centerFrame, textvariable=Name)
ID_Entry.grid(row=2,column=2)
amtTaken_Entry = Entry(centerFrame, textvariable=email)
amtTaken_Entry.grid(row=3,column=2)
IntPer_Entry = Entry(centerFrame, textvariable=numBer)
IntPer_Entry.grid(row=4,column=2)
# aDD_Entry = Entry(centerFrame, textvariable=aDD).grid(row=5,column=2)
TimePeriod_Entry = Entry(centerFrame,textvariable= timePeriod)
TimePeriod_Entry.grid(row=5,column=2)
PayDate_Entry = DateEntry(centerFrame, textvariable=aaDnumBer)
PayDate_Entry.grid(row=6,column=2)
ComTo_Entry = Entry(centerFrame, textvariable=pannumBer)
ComTo_Entry.grid(row=7,column=2)
ComPer_Entry = Entry(centerFrame, textvariable=bName)
ComPer_Entry.grid(row=8,column=2)
# accnumBer_Entry = Entry(centerFrame, textvariable=accnumBer)
# accnumBer_Entry.grid(row=9,column=2)

# TO SUBMIT THE FORM WE NEED A BUTTON DONT WE.
submit = Button(centerFrame, text="Register", command=register).grid(row=10, column=2)

window.mainloop()