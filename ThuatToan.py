from Class.ClassMyList import mylist
from Class.ClassNode import Node
from queue import PriorityQueue


'''@A 
param start: node - node bat dau
param goal: node - node ket thuc
param matrix: 2Dlist - ma tran chua cac diem
return list: neu co duong di
return False: neu khong co duong di
'''
def A(start:Node,goal:Node,matrix:list):
	# Tap hop nut mo
	open = PriorityQueue()

	# Tap hop nut dong
	close = mylist()

	# Dua nut start vao open
	open.put((start.f_n(goal),start))

	while not open.empty():
		x:Node = open.get()[1]

		# Tra ve ket qua
		if (x.x == goal.x) & (x.y == goal.y):
			result = list()
			while not x.parent == None:
				result.append(x)
				x = x.parent
			result.append(x)
			result.reverse()
			return result

		# Mo rong nut
		sub = x.subNode(matrix)
		close.append(x)
		for i in sub:
			if not close.is_containt(i):
				open.put((i.f_n(goal),i))
	return False


