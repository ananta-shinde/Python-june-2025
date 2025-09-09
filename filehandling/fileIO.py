
# creating a file
# to create a file you should use open() with either "w" or "a"

myfile = open("mydata.txt","w")

# writing into file to do this use write() or writeLines()
# single string writting
message = "this is my first line\n"
myfile.write(message)

message = "another message\n"
myfile.write(message)

#closing a file
myfile.close()

# reading file if it is open in "r" it is readonly and doesnot support writting
myfile = open("mydata.txt","r")

# myfile.write(message)

filedata =myfile.readlines()



print(filedata)