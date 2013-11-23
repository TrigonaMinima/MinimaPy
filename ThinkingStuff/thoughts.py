import random
import tkinter as tk

f = open('thoughts.txt', 'r')
g = open('data.txt', 'r')

#file containing all the quotes
thoughts = f.readlines()
f.close()

#file containing the quotes diaplayed in the past 30 days.
thought30 = g.readlines()
g.close()

if len(thought30) == 30:
	thought30.remove(0)
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
g.close()

#the quote displayed on the day using tkinter
root = tk.Tk()
w = tk.Label(root, text=todaysThought)
w.pack()
root.mainloop()
