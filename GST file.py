import os

class Gstgoods:
    productsNAME = "ABC"
    productPrice = 200
    productquantity = 100
    Gstpercentage = "percentage"


    def __int__(self, name, price, quantity, percentage ):
        self.productsNAME = name
        self.productPrice = price
        self.productquantity = quantity
        self.Gstpercentage = percentage

    def DisplayProductdetails(self):



        self.productsNAME = input("Enter the product name")
        self.productPrice = int(input("Enter the product price:"))
        self.productquantity = int(input("Enter the product quantity"))
        self.Gstpercentage = float(input("Enter the GST percentage"))

    def Displaydetails(self):
        print("The product detals are:" , "\n", self.productsNAME, "\n", self.productPrice, "\n" ,self.productquantity , "\n", self.Gstpercentage)

    #def Defaultconstructor(self):
     #   print("The Default constructor")

    def calculateGST(self):
        GST = (self.productPrice * self.Gstpercentage) / 100
        print("The GST on:" ,self.productsNAME, "is: ", GST)

emptyobj = Gstgoods()
emptyobj.Displaydetails()
emptyobj.DisplayProductdetails()
emptyobj.calculateGST()

print(os.getcwd())
my_file = open("C:\\Users\DELL 5480\PycharmProjects\pythonProject1\\gst.txt", "a+")
# import sys
# sys.stdout = open("C:\\Users\DELL 5480\PycharmProjects\pythonProject1\\gst.txt","w")
# sys.stdout.close()


while(True):
    productsNAME = input("Enter the product name")
    productPrice = int(input("Enter the product price:"))
    productquantity = int(input("Enter the product quantity"))
    Gstpercentage = float(input("Enter the GST percentage"))
    nextproduct = input("To  be continue or not: y/n")
    if (nextproduct == 'y' or nextproduct =='y'):
        continue
    else:
        break







