def phoneText(s):
	start = 0
	end = 0
	text = []
	while start < end:
		# find the lowest index of '#' between s[start,end]
		index = s.find('#',start,end)
		# find the substing
		sub = s[start:index]
		# find the last four available chars in the substring
		sub = sub[-4:]
		# find the input key
		key = sub[0]
		# find the length of substring
		l = len(sub)

		if l == 4:
			text.append(int(key))
