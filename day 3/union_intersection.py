def printUnion(arr1, arr2, m, n):
	if (m > n):
		tempp = arr1
		arr1 = arr2
		arr2 = tempp

		temp = m
		m = n
		n = temp
	arr1.sort()
	for i in range(0, m):
		print(arr1[i], end=" ")

	for i in range(0, n):
		if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1):
			print(arr2[i], end=" ")

def printIntersection(arr1, arr2, m, n):

	if (m > n):
		tempp = arr1
		arr1 = arr2
		arr2 = tempp

		temp = m
		m = n
		n = temp

	arr1.sort()
	for i in range(0, n):
		if (binarySearch(arr1, 0, m - 1, arr2[i]) != -1):
			print(arr2[i], end=" ")
def binarySearch(arr, l, r, x):

	if (r >= l):
		mid = int(l + (r - l)/2)

		if (arr[mid] == x):
			return mid	
		if (arr[mid] > x):
			return binarySearch(arr, l, mid - 1, x)		
		return binarySearch(arr, mid + 1, r, x)
	return -1
# main    
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
m = len(arr1)
n = len(arr2)
print("Union of two arrays is ")
printUnion(arr1, arr2, m, n)
print("\nIntersection of two arrays is ")
printIntersection(arr1, arr2, m, n)