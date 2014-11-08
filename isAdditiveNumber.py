def isAddNum(x):
	# split x into a list of digits
	A = [int(i) for i in str(x)]

	for l in range(1,len(A)/3+1):
		# compute the first two numbers a,b of length l
		a, b = 0, 0
		for i in range(l):
			a = A[i] + a*10
			b = A[i+l] + b*10
		# if a != b, continue looking for a,b of longer length
		if a != b: continue

		# if a == b, look for the third number c
		# set a pointer p for c
		p = 2*l
		c = 0

		while p < len(A):
			# compute the third possible number c
			c = A[p] + c*10
			# if we found the third number
			if (a+b) == c:
				# if p points to the last digit, return True
				if p == len(A)-1: 
					return True
				# else swap them and initialize c=0
				a = b
				b = c
				c = 0
			p = p + 1

	# if we don't find any additive number, return false
	return False

A = [112, 223, 12122436, 1313263965, 6612, 123123246, 1234567890]
for i in A:
	print str(i)+':', isAddNum(i)


