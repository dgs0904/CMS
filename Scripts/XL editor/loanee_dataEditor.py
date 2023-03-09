# Importing Modules 
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter
import sys,os
sys.path.append(os.path.abspath("C:/Users/golu6/Downloads/CMS/Scripts"))

# Declaring Variables.
lID = None
Name = None
email = None
numBer = None
aDD = None
aaDnumBer = None
pannumBer = None
bName = None
accnumBer = None

myListOfValues = [lID,Name,email,numBer,aDD,aaDnumBer,pannumBer,bName,accnumBer]


# Main Fucntions.
def detailWriter(lID,Name,email,numBer,aDD,aaDnumBer,pannumBer,bName,accnumBer):
    wb = load_workbook('./Scripts/personDetails.xlsx')
    ws = wb.active
    # To write new record about a loanee
    ws.append([lID,Name,email,numBer,aDD,aaDnumBer,pannumBer,bName,accnumBer])

    wb.save('./Scripts/personDetails.xlsx')

    print("wrote to workbook")