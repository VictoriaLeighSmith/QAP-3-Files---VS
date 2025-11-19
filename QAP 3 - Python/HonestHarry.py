# Description: Program to keep track of used car sales for Honest Harry's 
# Author: Victoria Smith
# Date(s): Nov 11 2025


# Define required libraries.
import datetime
import ValidateInputs as VI
import FormatValues as FV


# Define program constants.
CUR_DATE = datetime.datetime.now()

LIC_FEE_LOW_RATE = 75.00
LIC_FEE_HIGH_RATE = 165.00

TRANS_FEE_RATE = 0.01
LUX_TAX_FEE_RATE = 0.016

HST_RATE = 0.15


# Define program functions.
# Functions moved to Validate Inputs file.


# Main program starts here.
while True:
    
    # Gather user inputs.
    print()
    print()
    print(f"HONEST HARRY'S USED CAR LOT")
    print(f"Please enter the following:")
    print()

    # These inputs are all in Validate Inputs file.
    FirstName = VI.ValidateFirstName()

    if FirstName.upper() == "END":
        break

    LastName = VI.ValidateLastName()

    PhNum = VI.ValidatePhNum()

    PlateNum = VI.ValidatePlateNum()

    CarMake =    input("Enter the car make:                                  ")
    CarModel =   input("Enter the car model:                                 ")
    CarYear =    input("Enter the car year:                                  ")

    SellPrice = VI.ValidateSellPrice()

    TradePrice = VI.ValidateTradePrice(SellPrice)

    SalesName = VI.ValidateSalesName()
    

    # Perform required calculations.
    # Manipulate strings for receipt
    InvDate = datetime.datetime.strftime(CUR_DATE, "%b %d, %Y")

    CustName = FirstName[0:1] + ". " + LastName
    
    PhNumDsp = "(" + PhNum[0:3] + ") " + PhNum[3:6] + "-" + PhNum[6:]
    
    CarDetails = CarYear + " " + CarMake + " " + CarModel

    RecID = FirstName[0:1] + LastName[0:1] + "-" + PlateNum[3:6] + "-" + PhNum[6:]

    # Calculate program results
    AfterTrade = SellPrice - TradePrice
    
    if SellPrice <= 15000:
        LicFee = LIC_FEE_LOW_RATE
    else:
        LicFee = LIC_FEE_HIGH_RATE

    TransFee = SellPrice * TRANS_FEE_RATE

    if SellPrice > 20000:
        TransFee += (SellPrice * LUX_TAX_FEE_RATE)

    Subtotal = AfterTrade + LicFee + TransFee
    HSTAmt = Subtotal * HST_RATE
    Total = Subtotal + HSTAmt

    PayDay = CUR_DATE.day
    PayMonth = CUR_DATE.month + 1
    PayYear = CUR_DATE.year

    if PayDay >= 25:
        PayMonth += 1
    
    if PayMonth > 12:
        PayMonth -= 12
        PayYear += 1

    PayDate = datetime.datetime(PayYear, PayMonth, 1)


    # Display results
    print()
    print()
    print(f"Honest Harry Car Sales                           Invoice Date:   {InvDate:>12s}")
    print(f"Used Car Sales and Receipt                       Receipt No.:    {RecID:>12s}")

    print()
    print(f"                                          Sale Price:              {FV.FDollar2(SellPrice):>10s}")
    print(f"Sold to:                                  Trade Allowance:         {FV.FDollar2(TradePrice):>10s}")
    print(f"                                          -----------------------------------")
    print(f"      {CustName:<29s}       Price after Trade:       {FV.FDollar2(AfterTrade):>10s}")
    print(f"      {PhNumDsp:<14s}                      License Fee:             {FV.FDollar2(LicFee):>10s}")
    print(f"                                          Transfer Fee:            {FV.FDollar2(TransFee):>10s}")
    print(f"                                          -----------------------------------")
    print(f"Car Details:                              Subtotal:                {FV.FDollar2(Subtotal):>10s}")
    print(f"                                          HST:                     {FV.FDollar2(HSTAmt):>10s}")
    print(f"      {CarDetails:<29s}       -----------------------------------")
    print(f"                                          Total Sales Price:       {FV.FDollar2(Total):>10s}")
    print()
    print(f"-----------------------------------------------------------------------------")

    print()

    print(f"                                  Financing     Total        Monthly")
    print(f"        # Years    # Payments        Fee        Price        Payment")
    print(f"        ------------------------------------------------------------")

    for Year in range(1,5):
        NumMonPay = Year * 12
        FinFee = Year * 39.99
        TotPrice = Total + FinFee
        MonPayment = TotPrice / NumMonPay
        print(f"           {Year:>2d}          {NumMonPay:>2d}          {FV.FDollar2(FinFee):>7s}    {FV.FDollar2(TotPrice):>10s}   {FV.FDollar2(MonPayment):>9s}")

    print(f"        ------------------------------------------------------------")
    print(f"        First Payment Date: {FV.FDateM(PayDate)}")
    print(f"-----------------------------------------------------------------------------")
    print(f"{"Best used cars at the best prices!":^77s}")




