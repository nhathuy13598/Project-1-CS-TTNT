import math
#----------------------Class Node------------------------------------#
class Node():
	x = y = g = stt =0 # stt: thứ tự mở, g là chi phí, x,y là toạ độ
	parent = None

	# Hàm khởi tạo
	def __init__(self,x,y,parent):
		self.parent = parent
		self.x = x
		self.y = y

	# Hàm heuristic
	def heuristic(self,g):
		return math.sqrt(math.pow(g.x-self.x,2) + math.pow(g.y-self.y,2))

	# Hàm tính f(n)
	def f_n(self,g):
		return self.heuristic(g) + self.g

	# Hàm tính thứ tự mở
	def __lt__(self, other):
		if self.g < other.g:
			return True
		else:
			if (self.g == other.g) & (self.g < other.g):
				return True
		return False
#-----------------------End of Class Node----------------------------------#