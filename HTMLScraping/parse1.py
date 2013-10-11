from html.parser import HTMLParser
from html.entities import name2codepoint
import os.path
import urllib.request


url = "http://web-japps.ias.ac.in:8080/fellowship2014/selectfellows.jsp?atype=B&area=%25&col=Last_Name&searchtxt=Engineering"
fileName = "alpha.html"



class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		if not data == '\n':
			if "Available" in data or "Status" in data:
				g.write(data + '\n')
			else:
				if data.isalnum():
					g.write('(' + data + ')' + ' ') #, end = " "
				else :
					g.write(data.strip(' ').rstrip('\n') + ' ')# #, end = " "

parser = MyHTMLParser() #strict=False

g = open('parse1.txt', 'w+')

if not (os.path.isfile("/home/shivam/Desktop/html scraping/alpha.html")):
	f = open(fileName,'wb')
	with urllib.request.urlopen(url) as alpha:
		f.write(alpha.read())
	f.close()


with open('alpha.html', 'r') as f:
		line = f.readline()
		while not line == '' :
			parser.feed(line)
			line = f.readline()

f.close()
g.seek(0)
lines = g.readlines()
g.seek(0)

h = open('parsedCS.txt', 'w')
i = open('parsedPHYSICS.txt', 'w')
j = open('parsedSCIENCES.txt', 'w')
emb = open('parsedEMBEDDED.txt', 'w')
eng = open('parsedENGG.txt', 'w')

line = g.readline()
while not line == '' :
	if "Embedded" in line:
		emb.write(line + '\n')
	elif "Computer" in line :
		h.write(line + '\n')
	elif "Physics" in line :
		i.write(line + '\n')
	elif "Sciences" in line :
		j.write(line + '\n')
	elif "Engineering" in line :
		eng.write(line + '\n')
	line = g.readline()


h.close()
i.close()
j.close()
g.close()

g = open('parse1.txt', 'w')

word = ["Sciences","Physics","Embedded","Computer","Engineering", "Chemistry","Earth", "Metal"]

for line in lines:
	if not line == '\n':
		if not ((word[0] in line) or (word[1] in line) or (word[2] in line) or (word[3] in line) or (word[4] in line) or (word[5] in line) 
		or (word[6] in line) or (word[7] in line)) :
			g.write(line + '\n')
		

g.close()
