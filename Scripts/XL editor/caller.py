# Importing the modules that we are going to need
#from tkinter import goto,label

# Importing the file whose function we want to call/test
from idGenerator import *
from loanIdGenerator import *
from loanee_dataFinder import *
from loanee_dataEditor import *

tempId = None
name = None

# Calling The Function of File to save in a variable, passing Arguement
id = generateId(name)
loanId = generateLoanId(id)

# To find data of someone
def getData(loanIdId):
    myList = dataFinder(loanId)
    return myList


print(getData(loanId))
# print(id)s
# print(loanId)