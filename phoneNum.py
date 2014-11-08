def phoneNum(n,disallow):
	if n == 1:
		s = []
		for i in range(10):
			if i not in disallow:
				s.append([i])
		return s
	result = []
	for i in phoneNum(n-1,disallow):
		for j in limit(i,disallow):
			tmp = i[:]+[j]
			result.append(tmp)
	return result

def limit(a,disallow):
	s = []
	for i in range(10):
		if i not in disallow:
			if i != a[-1]:
				if a[0] != 4 and i==4:
					continue
				else:
					s.append(i)
	return s

def printPhoneNum(n,disallow):
	numList = phoneNum(n,disallow)
	for num in numList:
		print ''.join([str(i) for i in num])

printPhoneNum(2,[5,6,7])

