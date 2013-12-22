class Queue(object):
	def __init__(self):
		self.que = []
	def insert(self, e):
		self.que.append(e)
	def remove(self):
		try:
			return self.que.pop(0)
		except:
			raise ValueError('Queue is empty')
