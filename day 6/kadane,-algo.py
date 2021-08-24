def kadane_algo(a,size):
    	
	m1 = a[0]
	m2 = a[0]
	
	for i in range(0, size):
		m2 = m2 + a[i]
		if m2 < 0:
			m2 = 0
		
		
		elif (m1 < m2):
			m1 = m2
			
	return m1
a = [1,4,6,-7,8]    
size = len(a)
print("continuos sum of array is: ", kadane_algo(a, size))