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
	open.put((start.heuristic(goal),start))
	result = list()
	while not open.empty():
		print("Danh sach cac node")
		
		x:Node = open.get()[1]

		# Tra ve loi giai
		if (x.x == goal.x) & (x.y == goal.y):
			
			while not x.parent == None:
				result.append(x)
				x = x.parent
			result.append(x)
			result.reverse()
			return result

		# Mo rong nut
		close.append(x)
		sub = x.subNode(goal,close,matrix)
		for i in sub:
			if not close.is_contains(i):
				open.put((i.heuristic(goal),i))

		for item in list(open.queue):
			print("{0},{1}): f = {2},g = {3},stt = {4}".format(item[1].x,item[1].y,item[0],item[1].g,item[1].stt))
	return result



