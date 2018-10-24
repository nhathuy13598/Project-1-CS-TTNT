from Class.ClassMyList import mylist
from queue import PriorityQueue


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


