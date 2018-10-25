class mylist(list):
	# Kiem tra co ton tai phan tu other trong myList
	def is_containt(self,other):
		for i in self:
			if (i.x == other.x) & (i.y == other.y):
				return True
		return False
