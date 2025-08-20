numlist = [20,22,20,23,25,22]
# numlist = set(numlist)
# numlist = list(numlist)
myset =  set()
for x in numlist:
    myset.add(x)

numlist  = []
for x in myset:
    numlist.append(x)

print(numlist)