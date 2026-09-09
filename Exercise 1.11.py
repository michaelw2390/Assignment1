#(Population projection) The US Census Bureau projects population based on the
#following assumptions:
#One birth every 7 seconds
#One death every 13 seconds
#One new immigrant every 45 seconds
#Write a program to display the population for each of the next five years. Assume the
#current population is 312032486 and one year has 365 days. Hint: in Python, you
#can use integer division operator // to perform division. The result is an integer. For
#example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5)


CurrentPop = 312032486

secsPerMins = 60
minsPerHour = 60
hoursPerDay =  24
daysPerYear =  365
secsPerYear = secsPerMins * minsPerHour * hoursPerDay * daysPerYear


birth = secsPerYear//7
death =  secsPerYear//13
immigrant = secsPerYear//45

updatedPop = (immigrant + birth) - death

print("The population for the current year is", CurrentPop)
print("The Population for 2027 is", CurrentPop + updatedPop)
print("The population for 2028 is", CurrentPop + updatedPop + updatedPop)
print("The population for 2029 is", CurrentPop + updatedPop + updatedPop + updatedPop)
print("The population for 2030 is", CurrentPop + updatedPop + updatedPop + updatedPop + updatedPop)
print("The population for 2031 is", CurrentPop + updatedPop + updatedPop + updatedPop + updatedPop + updatedPop)

