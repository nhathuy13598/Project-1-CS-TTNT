import math

class Node():
	x = y = g = stt = 0 # stt: thứ tự mở, g là chi phí, x,y là toạ độ
	parent = None

	'''@__init__
	param x: int - toa do 
	param y: int - toa do
	param parent: node - node cha
	'''
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

	'''@check - kiem tra mot node co di duoc hay khong
	param x: int - hoanh do
	param y: int - tung do
	param data: 2Dlist - ma tran chua cac diem
	'''
	def check(self,data):
		size = len(data)
		if (self.x >= 0) and (self.x < size) and (self.y >= 0) and (self.y < size):
			if data[self.x][self.y] == 0:
				return True
		else:
			return False
	
	'''@subNode
	param data: 2Dlist - ma tran chua cac diem
	return: list - mang chua cac diem mo rong
	'''
	def subNode(self,data):
		x = [-1,-1,-1,0,1,1,1,0]
		y = [-1,0,1,1,1,0,-1,-1]
		sub = []
		for i in range(8):
			x_new = self.x + x[i]
			y_new = self.y + y[i]
			if self.check(data):
				a = Node(x_new,y_new,self)
				a.g = self.g + 1
				a.stt = i
				sub.append(a)
		return sub