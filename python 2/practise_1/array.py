from  array import *

arr = array("str",[])
x = int(input("No of elements: ")) 

print("Enter the values: ")
for i in range (x):
    n = str(input())
    arr.append(n) 
print("Array entered by user is",arr)
    