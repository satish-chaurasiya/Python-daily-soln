arr = [10,20,60,40,50]
arr.sort() #sorting
print(arr)
# for kth smallest no 
k = int(input('enter the value of k: '))
for i in range(0, len(arr)):
    if i is k-1:
        print('smallest', k ,'element' , arr[i])
#to find max 
arr1= arr[::-1]

print(arr)
k1=int(input('enter the value of k1'))
for i in range(0, len(arr1)):
    if i is k1-1:
        print('largest', k1 , 'element is ' , arr1[i])
 