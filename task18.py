#18) Write a Python class to convert an integer to a roman numeral.  
class irconvert:
    num_map=[(1000,'M'),(900,'CM'),(500,'D'),(100,"C"),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'IV'),(4,'IV'),(3,'III'),(2,'II'),(1,'I')]
    def NumToRoman(self,num):
        roman=""
        while num>0:
            for i,r in self.num_map:
                while num>=i:
                    roman+=r
                    num-=i
        return roman
num=int(input("Enter any Number : "))
print("Roman Number is : ",irconvert().NumToRoman(num))