n = int(input("enter number of values you want to add :"))
numlist = []
for x in range(n):
    num = int(input("enter a number"))
    numlist.append(num)

sum = 0
for x in numlist:
    sum = sum + x

print ("sum of values is : " +str(sum));