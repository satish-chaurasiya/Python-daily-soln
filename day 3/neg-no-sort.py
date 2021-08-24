
# function
def rearrange(arr, n ) :

	j = 0
	for i in range(0, n) :
		if (arr[i] < 0) :
			temp = arr[i]
			arr[i] = arr[j]
			arr[j]= temp
			j = j + 1
	print(arr)

# main code
arr = [-10, 20, -30, 40, 50, 16, -17, 48, -9]
n = len(arr)
rearrange(arr, n)



