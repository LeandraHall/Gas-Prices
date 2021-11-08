#'''This program solves the problem of 
#calculating the difference between cash and credit cost
#of buying N amount of gas'''
#Step 1 - Assign variable for credit price per gas = GasCreditPrice
#Step 2 - Assign variable for cash price per gas = GasCashPrice
#Step 3 - Assign variable for amount of gas through user input = N

#Asks user how much gas they would like to purchase
print("Hello. How much gas would you like to purchase?")
print("With cash, it's 2.79 per gallon.", end="")
print(" With credit, its 2.89 per gallon.")

#Variables for Equation
GasCreditPrice=2.89
GasCashPrice=2.79
N=input()

#Functions to find Prices of Gas
TotalPriceCredit=2.89*int(N)
TotalPriceCash=2.79*int(N)

#Prints total price with credit, total price with cash,
#and the difference between total credit price and cash price
print("The price you would pay for ", end="")
print( str(N) + " gallons of gas is " + str(TotalPriceCredit), end="")
print(" with credit card.")
print("With cash it's " + str(TotalPriceCash), end="")
print(". The price difference is " + str(TotalPriceCredit - TotalPriceCash) + ".")

