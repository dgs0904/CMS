# Importing Modules 
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter


# Declaring Variables.
# HERE WE WILL NOT NEED OTHER DETAILS LIKE NAME, EMAIL OR ID BECAUSE HERE WE'LL OPERATE ON LOAN ID WHICH CREATED ON THE BASIS OF OUR GENERAL ID.
lID = None
amount_taken = None
interestPerc = None
timePeriod = None
payDay = None
startDay = None
endDay = None
emiAmount = None
totalAmount = None
commTo = None
comPer = None
comRup = None
totalEmi= timePeriod

emi_Row = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','R','S','T','U','V','W','X','Y','X']

myListOfValues = [lID,amount_taken,interestPerc,timePeriod,payDay,startDay,endDay,emiAmount,totalAmount,commTo,comPer,comRup,totalEmi]

date_of_emi = None

# Main Fucntions.
def detailWriter(lID,amount_taken,interestPerc,timePeriod,payDay,startDay,endDay,emiAmount,totalAmount,commTo,comPer,comRup,totalEmi):
    wb = load_workbook('loanDetails.xlsx')
    ws = wb.active
    # To write new record about a loan
    ws.append([lID,amount_taken,interestPerc,timePeriod,payDay,startDay,endDay,emiAmount,totalAmount,commTo,comPer,comRup,totalEmi])
    
    # To find the line where the loan was registered and now all EMI blocks will be written out.
    # for row in range(1,10):
    #     # TO FIND THE ROW NUMBER OF LOAN DETAILS
    #     if lID == ws['A' + str(row)].value:
    #         working_row = row
    #     emi_var = 15

        # TO GO PARTICULAR BLOCKS TO PUT "PENDING" STATEMENT IN THE BEGGINING OF THE LOAD.
        # for emi in range(1,timePeriod):
        #     col = emi_Row[emi_var]

        #     # IF THIS IS LESS THAN 15 IT MEANS ALPHABET IS COMPLITED ONCE NOW WE ARE GOING IN COMPLEX ROW. EXAMPLE AA, AB, AC, ETC.
        #     if emi_var < 15:
        #         ws[ emi_Row[0]+ col + (row)].value = "pending"
            
        #     # THIS IS TO BE EXECUTED WHEN WE ARE IN THE FIRST ALPHABET STANCE.
        #     else:
        #         ws[ col + str(row)].value = "pending"
            
        #     # ONCE AN ALPHABET IS COMPLETED WE WILL RESET IT.
        #     if emi_var == 25:
        #         emi_var = 0
            
        #     # TO INCREMENT APLABET ONE BY ONE FOR EACH CELL.
        #     else:
        #         emi_var += 1

            


    wb.save('loanDetails.xlsx')


if __name__ == '__main__':
    detailWriter("20230225RA2502",5000,0.05,12,"01","02/01/23","02/01/24",437.5,5250,"Rahul","0.03",1.575,12)