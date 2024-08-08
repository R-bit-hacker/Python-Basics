import numpy as np
# lst1=[1,2,3,4,5]
# lst2=[2,3,4,5,6]
# lst3=[3,4,5,6,7]
# arr1=np.array([lst1,lst2,lst3])
# #print(arr1)
# #print(arr1[:,[0,-1]])
# #print(arr1<4)
# arr2=arr1.reshape(5,3)
# print(arr2)

#lists can't hold mathematical operations
lst1=[10,20,30]
lst2=[40,50,60]
print(lst1+lst2)
print(lst1*4)


#arrays using numpy can perform mathematical oeprations easily
a=np.array([20,30,40])
b=np.array([50,60,70])
print(a+b)
print(a*b)