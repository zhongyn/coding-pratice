def swap(i,j,s):
	if i > j:
		tem = i
		i = j
		j = tem
	return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]


def edit(a,b):
	i = 0
	j = 0
	l = len(a)
	while j < l:
		if b[j] == a[i]:
			if i == j:
				i += 1
				j += 1
			else:
				while i > j:
					a = swap(i,i-1,a)
					print a
					i -= 1
		else:
			i += 1

a = 'abc'
b = 'cab'
edit(a,b)