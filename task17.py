filename=input("Enter file name : ")
fh=open(filename)
lst=list()
words=[]
for line in fh:
    words+=line.split()
words.sort()
print("The unique words in aplhabetical order are : ")
for word in words:
    if word in lst:
        continue
    else:
        lst.append((word))
        print(word)
print(lst)

#Input file is file1.txt