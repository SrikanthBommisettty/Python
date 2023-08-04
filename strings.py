# strings

name = "srikanth"
print(type(name))
print ("The student name is:",name)
print("The 1st three letters is:",name[0:3])
#--.>to print name in reverse
print (name[::-1])
# to print length of string
print(len(name))
# to print it is a alpha numeric which contains both alphabets and numbers
print(name.isalnum())
# to print 1st character as capital
print(name.capitalize())
# to print the character by giving space
print(name.center(60))
name_1 = "balu babu 123123"
# to print the count value of b in between the range of 0 to 6 th index
print(name_1.count("b",0,6))
# to find the index value of a string
print(name_1.index("1"))
# to split the string so the given char will not get it print empty and remaining will print
print(name_1.split("b",3))
# to join a string
print(name_1.join("ABC"))




