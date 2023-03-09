# Importing All Necessary Modules
from datetime import date


def generateId(name):
    # Creating A Date Object
    dt = str(date.today())

    # Converting Date into String to Generate User Id
    dt = dt.replace('-','')

    # print(name.upper())
    name = dt + name[:2].upper()
    # Actuall ID to be used
    # print(name)
    return name


if __name__ == '__main__':
    generateId('Raj')