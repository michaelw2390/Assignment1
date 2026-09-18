# (Financial application: payroll) Write a program that reads the following infor-
# mation and prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)


name = (input("Enter your name: "))
hrsWorked = eval(input("Enter the hours worked: "))
rate = eval(input("Enter the rate of pay: "))
fedTax = eval(input("Enter the federal tax rate: "))/100
StateTax = eval(input("Enter the state tax rate: "))/100

grossPay = hrsWorked * rate
fedTaxes = grossPay * fedTax
stateTaxes = grossPay * StateTax

netPay = (grossPay - (fedTax * grossPay) - (StateTax * grossPay))

print("Employee's name: ", name)
print("Amount of hours worked: ", hrsWorked)
print("Rate of pay: ", rate)
print()
print("Deductions: ")
print("\tFederal tax withholding: ", fedTaxes)
print("\tState tax withholding: ", stateTaxes)
print("Net pay: ", netPay)


