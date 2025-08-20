numlist = [20,15,56,22,23]
num = int(input("enter number to search in list :"))
ispresent = False
for x in numlist:
    if (num == x):
        ispresent = True

if (ispresent == True):
    print("number is present")
else:
    print("number is not present")