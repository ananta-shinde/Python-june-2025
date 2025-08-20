sum = 0
for x in range(1,8):
   dayTemp = float(input("enter temp for day "+ str(x)))
   sum = sum + dayTemp
print(sum/7)