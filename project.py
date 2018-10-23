import math
from queue import PriorityQueue
import sys

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

# Mở file
def openfile(filename, mode):  
	try:
		with open(filename, mode):
			return open(filename, 'r')
	except IOError:
		print ("Could not read file:", filename)
		return False

# Đọc file
def readfile(filename):
	file = openfile(filename,"r")
	if file != False: 

		#sizeOfMatrix
		size = int(file.readline())

		#read start point
		a = file.readline()
		start = (int(a[:a.find(" ")]), int(a[a.find(" "):]))

		#read goal point
		a = file.readline()
		goal = (int(a[:a.find(" ")]), int(a[a.find(" "):]))

		#read matrix
		data = []
		for i in range(size):
			data.append([])
			d = file.readline()
			a = b = 0
			while (b < len(d)):
				if d[b] == " ":
					data[i].append(int(d[a:b]))
					a = b
				b += 1
			data[i].append(int(d[a:]))
		file.close()
		return (matrix(size,data),start,goal)
	else:
		return False

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

#--------------------------------Class MyList---------------------------------------#
class mylist(list):
	def is_containt(self,other):
		for i in self:
			if (i.x == other.x) & (i.y == other.y):
				return True
		return False
#--------------------------------End of Class Mylist--------------------------------#

#---------------------------Thuật toán tìm đường đi--------------------------------#
def A(start,goal,matrix):
	open = PriorityQueue()
	close = mylist()#opened node
	open.put((start.f_n(goal),start))
	while not open.empty():
		x = open.get()[1]
		if (x.x == goal.x) & (x.y == goal.y):
			result = list()
			while not x.parent == None:
				result.append(x)
				x = x.parent
			result.append(x)
			result.reverse()
			return result
		sub = matrix.subNode(x)
		close.append(x)
		for i in sub:
			if not close.is_containt(i):
				open.put((i.f_n(goal),i))
	return False
#---------------------------Kết thúc thuật toán tìm đường đi----------------------------#


#-------------------------------Ghi file-------------------------------------------#
def writeFile(filename,mode, data):
	file = open(filename, mode)
	if file != False:
		file.write(int.__str__(data[0])+'\n')
		for i in data[2]:
			file.write("({0},{1}) ".format(i.x,i.y))
		file.write("\n")
		for i in range(data[1].size):
			str = ""
			for j in range(data[1].size):
				
				if (i == data[3].x) & (j == data[3].y):
					str = str + "S "
				elif data[2].is_containt(Node(i,j,None)):
					str = str + "x "
				elif i == data[4].x & j == data[4].y:
					str = str + "G "
				else:
					if data[1].data[i][j] == 0:
						str = str + "- "
					else:
						str = str + "o "
			file.write(str+'\n')
		else: 
			return False
#----------------------------------Kết thúc ghi file---------------------------------------#


# Hàm main
def main():
	if(len(sys.argv) == 3):
		file = readfile(sys.argv[1])
		if not file: 
			print("Error!!!")
			return
		start = Node(file[1][0],file[1][1],None)
		goal = Node(file[2][0],file[2][1],None)
		matrix = file[0]
		result = mylist(A(start,goal,matrix))
		f = writeFile(sys.argv[2],"w", (len(result),matrix,result,start,goal))
		if not f:
			print("Error!!!")
	else:
		print("Error!!!")
main()