import numpy as np

zeroArray = np.array(800)
zeroArray1 = np.array(200)
resultArray = zeroArray + zeroArray1
resultArray2 = zeroArray - zeroArray1
resultArray3 = zeroArray // zeroArray1
resultArray4 = zeroArray % zeroArray1
print("The resultArray dimension array dimension is : ", resultArray.ndim)
print("The addition of two zero arrays is: ",resultArray)
print("\n .........................................................")
print("The zero dmension aray is: ",zeroArray)
print("The zero dimension array dimension is: ",zeroArray.ndim)
print("The number of elements in zero dimension array is : ",zeroArray.size)
print("The zero dimension array shape is: ",zeroArray.shape)
print("\n ..............................................................")
print("The result array dimensions : \n", resultArray)
print("The dimenson of zero dimensional array1 is : \n" , resultArray.ndim)
print("The number of elements in zero dimension array is : ",resultArray.size)
print("The zero dimension array shape is : ",resultArray.shape)
print("\n ..................................................................")
print("The result array dimension s: \n", resultArray2)
print("The dimenson of zero dimensional array1 is : \n" , resultArray2.ndim)
print("The number of elements in zero dimension array is : ",resultArray2.size)
print("The zero dimension array shape is : ",resultArray2.shape)
print("\n ...................................................................")
print("The result array dimension s: \n", resultArray3)
print("The dimenson of zero dimensional array1 is : \n" , resultArray3.ndim)
print("The number of elements in zero dimension array is : ",resultArray3.size)
print("The zero dimension array shape is : ",resultArray3.shape)
print("\n ....................................................................")
print("The result array dimension s: \n", resultArray4)
print("The dimenson of zero dimensional array1 is : \n" , resultArray4.ndim)
print("The number of elements in zero dimension array is : ",resultArray4.size)
print("The zero dimension array shape is : ",resultArray4.shape)
print("\n ....................................................................")
