def wellOrderedLower(n,l):
	if n<=0 or n>26:
		print 'please input an integer between 1 and 26'
	if n == 1:
		# return a list of a to z
		return [chr(i) for i in range(ord('a'),ord('z')-l+n+1)]

	result = []
	# for each item in wellOrdered(n-1), 
	# if its last character is before 'z',
	# we concatenate a possible charater to the item,
	# and add this new item to result.
	for prefix in wellOrderedLower(n-1,l):
		for i in range(ord(prefix[-1])+1,ord('z')+2-(l-(n-1))):
			result.append(prefix+chr(i))
	return result

def wellOrdered(n):
	s = wellOrderedLower(n,n)
	print len(s)
	result = []
	for word in s:
		result.extend(addUpper(word))
	return result

def addUpper(w):
	if len(w) == 1:
		return [w,w.upper()]
	result = []
	for i in addUpper(w[1:]):
		result.append(w[0]+i)
		result.append(w[0].upper()+i)
	return result

# result = wellOrdered(26)
result = wellOrderedLower(13,13)
# print result
# print result
print len(result)
