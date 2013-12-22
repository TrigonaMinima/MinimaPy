
def chk(s):
	alpha = 'abcdefghijklmnopqrstuvwxyz '
	i = 0
	while i < len(s):
		substr1 = substr2 = ''
		if s[i] in alpha :
			substr2 = ''
			#substr2 = substr2 + s[i]
			j = i
			a = alpha.find(s[i])
			while j < len(s):
				if alpha.find(s[j], a) :
					a = alpha.find(s[j])
					substr2 = substr2 + s[j]
					j = j+1
				else :
					break
		if len(substr1) < len(substr2) :
			substr1 = substr2
		i = i+1
	print 'Longest substring in alphabetical order is : ', substr1
	
	
s = 'jhpbzbajnchufmqfia'
chk(s)
