from Class.ClassNode import Node


#---------------------------------Class Matrix-----------------------------#
class matrix:
	size = 0
	data = None
	def __init__(self,size,data):
		self.size = size
		self.data = data
	def check(self,x,y):
		if (x >= 0) & (x<self.size) & (y>=0) & (y<self.size):
			if self.data[x][y] == 0:
				return True
		else:
			return False
	def subNode(self,node):
		x = [-1,-1,-1,0,1,1,1,0]
		y = [-1,0,1,1,1,0,-1,-1]
		sub = []
		for i in range(8):
			x_new = node.x+x[i]
			y_new = node.y+y[i]
			if self.check(x_new,y_new):
				a = Node(x_new,y_new,node)
				a.g = node.g+1
				a.stt = i
				sub.append(a)
		return sub
#-----------------------------------End of Class Matrix------------------------------#