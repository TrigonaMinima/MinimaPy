import random
import func
import datetime as date

quotesFile = 'thoughts.txt'

f = open(quotesFile, 'r')
g = open('data.txt', 'r')

#reading containing all the quotes
thoughts = f.readlines()
f.close()

#list of the quotes diaplayed in the past month.
thought30 = g.readlines()
g.close()

d = date.datetime.now()
if len(thought30)>1 and str(d.day) == thought30[-1]:
	todaysThought = thought30[-2]
else:
	if thought30:
		thought30.pop(-1)
	if len(thought30) > 28:
		thought30.pop(0)
	while 1:
		todaysThought = thoughts[random.randrange(0, len(thoughts))]
		if todaysThought in thought30:
			continue
		else:
			thought30.append(todaysThought)
			break
	g = open('data.txt', 'w')
	for line in thought30:
		g.write(line)
	g.write(str(d.day))
	g.close()
func.output(todaysThought)
