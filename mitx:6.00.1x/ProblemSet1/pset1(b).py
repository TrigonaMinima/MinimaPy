def chk(s) :
	i = 0
	s = s+' '
	substr1 = substr2 = ''
	for i in range(0, len(s)) :
		substr2 = ''
		for j in range(i, len(s)-1):
			if ord(s[j]) <= ord(s[j+1]):
				substr2 = substr2 + s[j]
			else :
				break
		substr2 = substr2 + s[j]
		if len(substr1) < len(substr2) :
			substr1 = substr2
	print 'Longest substring in alphabetical order is : ', substr1


s = 'abcdefghijklmnopqrstuvwxyz'
s = 'xfewalkepwxpfbxvhuakrhc'
chk(s)
