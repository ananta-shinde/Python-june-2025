numlist  = [20,45,56,25,23,22]
# num = 56

def list_contains(list,num):
    for x in list:
        if (x == num):
            return True
    return False



def list_delete(list,value):
    result= list_contains(list,value)
    print(result)
    if( result == True):
        list.remove(value)
        return True
    else:
       return False


# def list_indexOf(list,value):
#     foundindex = -1
#     count = 0
#     for x in numlist:
#         if (x == value):
#             foundindex = count
#         count = count + 1
#     return foundindex

def list_indexOf(list,value):
    index = -1
    for x in  range(len(list)):
        if(list[x] == value):
            index = x
    return index

def list_filter(list):
    newList = []
    for x in list:
        if(x <=50):
            newList.append(x)
    return newList


def list_print(list):
    for x in list:
        print(x)

def list_update(list,oldvalue,newvalue):
    index = list_indexOf(list,oldvalue)
    if(index == -1):
        list.append(newvalue)
    else:
        list[index] = newvalue




list_update(numlist,100,55)
print(numlist)





