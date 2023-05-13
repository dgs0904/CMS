from tkinter import *
import sys
import os
sys.path.append(os.path.abspath("./Scripts/XL editor"))
from idGenerator import *
from loanIdGenerator import *
from loanee_dataFinder import *
from loanee_dataEditor import *
from email_alert import *

def main():
    window = Tk()
    window.geometry("960x550")
    window.configure(bg="white")
    window.title("Borrowers")

    def loanSearchFrame(selectionWindow):
        window.destroy()
        selectionWindow.destroy()
        import loan_search
        loan_search.main()

    def loanCreationFrame(selectionWindow):
        window.destroy()
        selectionWindow.destroy()
        import new_loan_registration_form
        new_loan_registration_form.main()

    def loaneeSearchFrame(selectionWindow):
        window.destroy()
        selectionWindow.destroy()
        import loanee_search
        loanee_search.main()

    def loaneeCreationFrame(selectionWindow):
        window.destroy()
        selectionWindow.destroy()
        import new_loanee_registration_form
        new_loanee_registration_form.main()

    def borrowerSelectionFrame():
        selectionWindow = Tk()
        selectionWindow.geometry("300x200+100+200")
        selectionWindow.title("Select an option")
        selectionWindow.rowconfigure(0, weight=1)
        selectionWindow.columnconfigure(0, weight=1)
        selectionWindow.columnconfigure(1, weight=1)

        btn_searchLoan = Button(selectionWindow, text="Search for Borrowers", command=lambda: loaneeSearchFrame(selectionWindow))
        btn_searchLoan.grid(row=0,column=0, sticky="NEWS", padx=10, pady=10)
        btn_createLoan = Button(selectionWindow, text="Create a Borrower", command=lambda : loaneeCreationFrame(selectionWindow))
        btn_createLoan.grid(row=0,column=1, sticky="NEWS", padx=10, pady=10)
        
        selectionWindow.mainloop()

    def loanSelectionFrame():
        selectionWindow = Tk()
        selectionWindow.geometry("300x200+100+200")
        selectionWindow.title("Select an option")
        selectionWindow.rowconfigure(0, weight=1)
        selectionWindow.columnconfigure(0, weight=1)
        selectionWindow.columnconfigure(1, weight=1)

        btn_searchLoan = Button(selectionWindow, text="Search for Loans", command=lambda: loanSearchFrame(selectionWindow))
        btn_searchLoan.grid(row=0,column=0, sticky="NEWS", padx=10, pady=10)
        btn_createLoan = Button(selectionWindow, text="Create a Loan", command=lambda : loanCreationFrame(selectionWindow))
        btn_createLoan.grid(row=0,column=1, sticky="NEWS", padx=10, pady=10)
        
        selectionWindow.mainloop()

    def paymentFrame():
        window.destroy()
        import Payments_Page
        Payments_Page.main()

    def homeFrame():
        window.destroy()
        import home_gui
        home_gui.main()

    # VARIABLES TO BE USED IN LOANEE REGISTRATION.
    ID = StringVar()
    # Name = StringVar()
    # email = StringVar()
    # numBer = IntVar()
    # aDD = StringVar()
    # aaDnumBer = IntVar()
    # pannumBer = IntVar()
    # bName = StringVar()
    # accnumBer = IntVar()
    # amount = IntVar()

    # METHOD TO CALL LOANEE_DATAEDITOR.PY AND REGISTER THE USER.
    def search():
        # TO GET THE ID OF THE PERSON WHOSE DATA WE WANT TO FIND.
        ID = ID_Entry.get()


        # THIS SECTION IS FOR CHECKING IF THE CODE TILL HERE IS WORKING OR NOT.
        # if ID == "":
        #     print("Something is fishy, not reading user entered value")
        # else:
        #     print("Nothing looks bad for now")

        myListOfData = dataFinder(ID)
        
        myListOfValues = [ID,fName,email,numBer,aDD,aaDnumBer,pannumBer,bName,accnumBer]
        
        for i in range(0,len(myListOfValues)):
            myListOfValues[i] = myListOfData[i]


        ID_label = Label(centerFrame, text="ID",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=3, column=1, padx=100, pady =5)
        ID_label = Label(centerFrame, text=myListOfValues[0],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=3, column=2, padx=100, pady =5)

        Name_label = Label(centerFrame, text="Name",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=4, column=1, padx=100, pady =5)
        Name_label = Label(centerFrame, text=myListOfValues[1],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=4, column=2, padx=100, pady =5)
        
        Email_label = Label(centerFrame, text="Email",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=5, column=1, padx=100, pady =5)
        Email_label = Label(centerFrame, text=myListOfValues[2],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=5, column=2, padx=100, pady =5)

        Number_label = Label(centerFrame, text="Mobile Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=6, column=1, padx=100, pady =5)
        Number_label = Label(centerFrame, text=myListOfValues[3],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=6, column=2, padx=100, pady =5)

        Address_label = Label(centerFrame, text="Address",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=7, column=1, padx=100, pady =5)
        Address_label = Label(centerFrame, text=myListOfValues[4],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=7, column=2, padx=100, pady =5)

        AadhaarCard_label = Label(centerFrame, text="Aadhaar Card Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=8, column=1, padx=100, pady =5)
        AadhaarCard_label = Label(centerFrame, text=myListOfValues[5],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=8, column=2, padx=100, pady =5)

        PanCard_label = Label(centerFrame, text="Pancard Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=9, column=1, padx=100, pady =5)
        PanCard_label = Label(centerFrame, text=myListOfValues[6],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=9, column=2, padx=100, pady =5)

        BankName_label = Label(centerFrame, text="Bank Name",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=10, column=1, padx=100, pady =5)
        BankName_label = Label(centerFrame, text=myListOfValues[7],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=10, column=2, padx=100, pady =5)

        AccountNumber_label = Label(centerFrame, text="Account Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=11, column=1, padx=100, pady =5)
        AccountNumber_label = Label(centerFrame, text=myListOfValues[8],font="ariel 10 ",bg= "white", justify= LEFT).grid(row=11, column=2, padx=100, pady =5)
        





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
    home_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Home", command=homeFrame)
    home_button.pack(pady=10, padx=50)

    borrowers_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Borrowers", command=borrowerSelectionFrame)
    borrowers_button.pack(pady=10,padx=50)

    loans_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Loans", command=loanSelectionFrame)
    loans_button.pack(pady=10,  padx=50)

    payments_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Payments", command=paymentFrame)
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

    search_label = Label(centerFrame, text="Identity Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=2, column=1, padx=100, pady =5)

    # Email_label = Label(centerFrame, text="Email",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=3, column=1, padx=100, pady =5)

    # Number_label = Label(centerFrame, text="Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=4, column=1, padx=100, pady =5)

    # Address_label = Label(centerFrame, text="Address",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=5, column=1, padx=100, pady =5)

    # AadhaarCard_label = Label(centerFrame, text="Aadhaar Card",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=6, column=1, padx=100, pady =5)

    # PanCard_label = Label(centerFrame, text="PanCard Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=7, column=1, padx=100, pady =5)

    # BankName_label = Label(centerFrame, text="Bank Name",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=8, column=1, padx=100, pady =5)

    # AccountNumber_label = Label(centerFrame, text="Account Number",font="ariel 10 ",bg= "white", justify= LEFT).grid(row=9, column=1, padx=100, pady =5)







    # TEXT ENTRY WIDGETS IN CENTERFRAME.
    # loanId_Entry = Entry(centerFrame, textvariable=lID).grid(row=1,column=2)
    ID_Entry = Entry(centerFrame, textvariable=Name)
    ID_Entry.grid(row=2,column=2)
    # email_Entry = Entry(centerFrame, textvariable=email)
    # email_Entry.grid(row=3,column=2)
    # numBer_Entry = Entry(centerFrame, textvariable=numBer)
    # numBer_Entry.grid(row=4,column=2)
    # # aDD_Entry = Entry(centerFrame, textvariable=aDD).grid(row=5,column=2)
    # aDD_Entry = Text(centerFrame, height=2, width=40)
    # aDD_Entry.grid(row=5,column=2)
    # aaDnumBer_Entry = Entry(centerFrame, textvariable=aaDnumBer)
    # aaDnumBer_Entry.grid(row=6,column=2)
    # pannumBer_Entry = Entry(centerFrame, textvariable=pannumBer)
    # pannumBer_Entry.grid(row=7,column=2)
    # bName_Entry = Entry(centerFrame, textvariable=bName)
    # bName_Entry.grid(row=8,column=2)
    # accnumBer_Entry = Entry(centerFrame, textvariable=accnumBer)
    # accnumBer_Entry.grid(row=9,column=2)

    # TO SUBMIT THE FORM WE NEED A BUTTON DONT WE.
    submit = Button(centerFrame, text="Find Loanee", command=search).grid(row=2, column=3)

    window.mainloop()