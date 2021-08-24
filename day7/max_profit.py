def maxprofit(arr, n):
    maxprofit = 0
    for i in range(0,n):
       maxprofit = arr[i+1] - arr[i]
       if maxprofit>0:        
            return maxprofit

  
           
            
    


arr = [3,5,7,4,8]
n = len(arr)
print(maxprofit(arr, n))



       
        