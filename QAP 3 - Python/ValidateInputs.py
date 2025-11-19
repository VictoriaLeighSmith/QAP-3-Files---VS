# Description: Library of validation functions. Moved to separate file to keep main program neat and tidy.
# Author: Victoria Smith
# Date(s): Nov 14 2025


# Generic funciton to check for an empty string - this way, this bit of code is not repeated over and over in the main program.
def CheckIfBlank(Prompt, ErrorMessage):
    while True:
        Value = input(Prompt)

        if Value == "":
            print(ErrorMessage)
        else:
            break

    return Value

def ValidateFirstName():
    FirstName = CheckIfBlank(f"Enter customer first name (END to exit):             ",
                             " ** Data Entry Error: Customer first name cannot be blank. ** ")
    
    return FirstName.title()

def ValidateLastName():
    LastName = CheckIfBlank(f"Enter customer last name:                            ", 
                            " ** Data Entry Error: Customer last name cannot be blank. ** ")
    
    return LastName.title()

def ValidatePhNum():
    while True:
        PhNum = CheckIfBlank(f"Enter the phone number (5555555555):                 ", 
                             " ** Data Entry Error: Phone number cannot be blank. ** ")

        if len(PhNum) != 10:
            print(f" ** Data Entry Error: Phone number must be 10 digits. ** ")
        elif PhNum.isdigit() == False:
            print(f" ** Data Entry Error: Phone number must be digits only. ** ")
        else:
            break

    return PhNum

def ValidatePlateNum():
    while True:
        PlateNum = CheckIfBlank(f"Enter the plate number (XXX999):                     ", 
                                " ** Data Entry Error: Plate number cannot be blank. ** ")
        
        if len(PlateNum) != 6:
            print(f" ** Data Entry Error: Plate number must be 6 characters. ** ")
        elif not (PlateNum[0:3].isalpha() and PlateNum[3:6].isdigit()):
            print(f" ** Data Entry Error: Plate number must be in XXX999 format. ** ")
        else:
            break

    return PlateNum.upper()

def ValidateSalesName():
    SalesName = CheckIfBlank(f"Enter the salesperson name:                          ",
                             " ** Data Entry Error: Salesperson name cannot be blank. ** ")
    
    return SalesName.title()

# Created a generic function here to validate that the value given is a numeric value that can be converted to a float. 
def ValidatePrices(Prompt, ErrorMessage):
    while True:
        try:
            Value = input(Prompt)
            Value = float(Value)
        except:
            print(ErrorMessage)
        else:
            break

    return Value

# Separate functions for value specific validation.
def ValidateSellPrice():
    while True:
        SellPrice = ValidatePrices(f"Enter the selling price (max $50,000):               ", 
                                " ** Data Entry Error: Selling price must be numeric value. ** ")
        
        if SellPrice > 50000:
                    print(f" ** Data Entry Error: Selling price cannot exceed $50,000. ** ")
        else:
            break

    return SellPrice

def ValidateTradePrice(SellPrice):
    while True:
        TradePrice = ValidatePrices(f"Enter the trade in price:                            ", 
                                    " ** Data Entry Error: Trade in price must be numeric value. ** ")
        if TradePrice > SellPrice:
                print(f" ** Data Entry Error: Trade in price cannot be greater than selling price. ** ")
        else:
            break

    return TradePrice    












