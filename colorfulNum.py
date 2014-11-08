def isColorfulNum(x):
	# split x into a list of digits
	A = [int(i) for i in str(x)]
	# init a list of substring values
	products = []

	# compute the product of substring of length l 
	for l in range(1,len(A)):
		j = 0
		while j+l<=len(A):
			tem = digitsProduct(A[j:j+l])
			if tem in products:
				return False
			else:
				products.append(tem)
			j = j+1
	return True

def digitsProduct(s):
	product = 1	
	for i in s:
		product *= i 
	return product

print isColorfulNum(2355)

