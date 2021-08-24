# creating a function 
def diff(arr,k):
    for i in range(0,len(arr)):
        if arr[i]-k<0:
            arr[i] = arr[i]+k
        else:
            arr[i]= arr[i]-k    
    print(max(arr)-max(arr))



#main code
arr = [1,3,6,8,9]
print('original array', arr)
k = 4
diff(arr, k)
print('final array',sorted(arr))