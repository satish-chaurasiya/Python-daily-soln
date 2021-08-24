def rotat(arr ,n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp    
      
# main code
arr = [4 ,5,6,8,9,45,356]   
n = len(arr)     
print('this is the orininal array', arr)
rotat(arr, n)
print('this is the array rotated by 1',arr)
