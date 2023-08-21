import numpy as np

oneArray = np.array([1000,222])
print("The one dmension aray is: ",oneArray)
print("The one dimension array dimension is: ",oneArray.ndim)
print("The number of elements in zero dimension array is : ",oneArray.size)
print("The one dimension array shape is: ",oneArray.shape)
print("\n ...........................................")


oneArray1 = np.array([10,20,30,40])
oneArray2 = np.array([-20,-11,-33,-44])
resultarray1 = oneArray1 - oneArray2
resultarray2 = oneArray1 + oneArray2
resultarray3 = oneArray1 % oneArray2
print("The one dmension aray is: ",oneArray1)
print("The one dimension array dimension is: ",oneArray1.ndim)
print("The number of elements in one dimension array is : ",oneArray1.size)
print("The one dimension array shape is: ",oneArray.shape)
print("\n .................................................................")
print("The result array dimension s: \n", resultarray1)
print("The dimenson of one dimensional array1 is : \n" , resultarray1.ndim)
print("The number of elements in one dimension array is : ",resultarray1.size)
print("The one dimension array shape is : ",resultarray1.shape)
print("\n ....................................................................")
print("The result array dimension s: \n", resultarray2)
print("The dimenson of one dimensional array1 is : \n" , resultarray2.ndim)
print("The number of elements in one dimension array is : ",resultarray2.size)
print("The one dimension array shape is : ",resultarray2.shape)
print("\n ...................................................................")
print("The result array dimension s: \n", resultarray3)
print("The dimenson of one dimensional array1 is : \n" , resultarray3.ndim)
print("The number of elements in one dimension array is : ",resultarray3.size)
print("The one dimension array shape is : ",resultarray3.shape)
print("\n ...................................................................")






