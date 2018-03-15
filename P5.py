#Parker Smith
#2/19/2018
#CCIS 1505-02
#Program 5

#Print number of letters in name
strName = input("Please enter your first and last name: ")
intLen = len(strName)
print ("Your name has", intLen, "characters in it!")
print()

#Months of the year as a string
tupMonNames = ("January","Febuary","March","April","May","June","July","August","September","October","November","December")

#Loop and slicing of the months
for month in tupMonNames:
    print(month + " = " + month[0:3])
print()

#Display months that start with J
for month in tupMonNames:
    if month.startswith("J"):
        print(month)
print()

#Search months and see if it is there
strMonth = input("Enter a month: ")
if strMonth.title() in tupMonNames:
    print ("Month found.")
else:
    print ("Month not found.")
print()

#Print users name 10 times with loop counter
strNme = input("Please enter your first name: ")
count = 1
for intLoop in range(1, 11, 1):
    print (strNme, "loop counter = ", intLoop)
print()

#Count 1-19 only odd numbers
for intLC in range(1, 20, 2):
    print (intLC)


