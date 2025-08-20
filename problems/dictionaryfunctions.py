data = {}

# insert
data["rollNo"] = 20
data["name"] = "Ananta"

# update
data["rollNo"] = 50

def dict_replace(dict,oldvalue,newvalue):
    key = dict_getkey(data,oldvalue)
    if(key != None):
        dict[key]= newvalue

#delete
# data.pop("rollNo")

def dict_delete(dict,value):
    key = dict_getkey(data,value)
    data.pop(key)

def dict_getkey(dict,value):
    key = None
    for x in dict:
        if(dict[x] == value):
            key = x
    return key


#print
def dict_print(dict):
    for x in dict:
        print(dict[x])

#


dict_replace(data,50,40)
dict_replace(data,"Ananta","Rahul")


print(data.keys())