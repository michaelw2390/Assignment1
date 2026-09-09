# (Financial application: calculate future investment value) Write a program that
# reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value using the following formula:
# Enter investment amount:
# Enter annual interest rate:
# Enter number of years:
# Accumulated value is 1043.33



invAmt = eval(input("Enter investment amount: "))
apy = eval(input("Enter interest rate: "))
years = eval(input("Enter number of years: "))

value = invAmt * apy/100 * years

print("The accumulated value is", invAmt + value)
