# (Reverse number) Write a program that prompts the user to enter a four-digit inte-
# ger and displays the number in reverse order. Here is a sample run:




num = int(input(" Enter an Integer: "))

one = num % 10
num = num // 10

two = num % 10
num = num // 10

three =num % 10
num = num // 10

four = num % 10
num = num // 10

print("The reversed number is: ", one,two,three,four)





