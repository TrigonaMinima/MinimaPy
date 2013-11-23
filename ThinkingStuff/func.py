#the quote displayed on the day using tkinter
import tkinter as tk

def output(string):
	root = tk.Tk()
	pos = string.find('-', 0, len(string))
	w = tk.Label(root, text=string[0:pos])
	w.pack()
	q = tk.Label(root, text=string[pos:len(string)])
	q.pack()
	root.mainloop()
