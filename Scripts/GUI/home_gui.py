from tkinter import *

def main():
    window = Tk()
    window.geometry("960x540")
    window.title("CMS")

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

    borrowers_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Borrowers", command=borrowerSelectionFrame)
    borrowers_button.pack(pady=10,padx=50)

    loans_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Loans", command=loanSelectionFrame)
    loans_button.pack(pady=10,  padx=50)

    payments_button = Button(outlinerFrame, background="black",fg="white",width=20, text="Payments", command= paymentFrame)
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
    Payments_button = Button(centerFrame,height=2,width=20,fg="white",bg="#0694bc" ,text="View Payments", command= paymentFrame)
    Payments_button.pack(pady=50,  padx=40 , side=LEFT)

    Borrowers_button = Button(centerFrame,height=2,width=20,fg="white",bg="#0c9c3a" ,text="View Borrowers", command= borrowerSelectionFrame)
    Borrowers_button.pack(pady=50,  padx=40 , side=LEFT)

    Loans_button = Button(centerFrame,height=2,width=20,fg="white",bg="#8221c4", text="View Loans", command=loanSelectionFrame)
    Loans_button.pack(pady=50,  padx=40 , side=LEFT)
    window.mainloop()

if __name__ == "__main__":
    main()