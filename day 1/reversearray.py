lst = []  
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())

	lst.append(ele)
	
print(lst)
for i in range(0, len(lst)):    
    print(lst[i]),     
print("Array in reverse order: ");    
#Loop through the array in reverse order    
for i in range(len(lst)-1, -1, -1):     
    print(lst[i])

print(lst)    