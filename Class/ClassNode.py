import math

class Node():
	f = stt = g = 0 # stt: thứ tự mở, f là chi phí, g là bước đi
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
	def heuristic(self,goal):
		return math.sqrt(math.pow(goal.x-self.x,2) + math.pow(goal.y-self.y,2))

	# Hàm tính thứ tự mở
	def __lt__(self, other):
		if self.f < other.f:
			return True
		elif self.f == other.f and self.stt < self.stt:
			return True
		return False

	'''@subNode
	param goal: node - node dich
	param data: 2Dlist - ma tran chua cac diem
	return: list - mang chua cac diem mo rong
	'''
	def subNode(self,goal,closedNode,data:list):
		size = len(data)
		x = [-1,-1,-1,0,1,1,1,0]
		y = [-1,0,1,1,1,0,-1,-1]
		sub = []
		for i in range(8):
			x_new = self.x + x[i]
			y_new = self.y + y[i]
			if (x_new >= 0) and (x_new < size) and (y_new >= 0) and (y_new < size):
				if data[x_new][y_new] == 0:
					a = Node(x_new,y_new,self)
					a.g = 1
					a.f = a.heuristic(goal) + a.g
					a.stt = i
					sub.append(a)
		return sub