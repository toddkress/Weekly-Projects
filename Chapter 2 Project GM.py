## This is the start of the program
## iP is the Item Price and cP is the Customer Price
## Customers will enter currancy values in whole numbers
iP=int(input('Please enter the total cost of the customers purchase:'))
cP=int(input('Please enter what the customer paid:'))
## Program will subtract out the item price from the customers pay to allow for change calculation
## cH stands for Change
cH=(cP-iP)
## Dividing Change by the subtracted total
## Change will be displayed by numeric value after printed change value
## Fives will be displayed after the following calculation
print("Amount of fives =", cH//500)

cH = cH%500
## Ones will be displayed after the following calculation
print("Amount of ones =", cH//100)

cH = cH%100
## Quarters will be displayed after the following calculation
print("Amount of quarters =", cH//25)

cH = cH%25
## Dimes will be displayed after the following calculation
print("Amount of dimes =", cH//10)

cH = cH%10
## Nickles will be displayed after the following calculation
print("Amount of nickles =", cH//5)

cH = cH%5
## Pennies will be displayed after the following calculation
print("Amount of pennies =", cH//1)


