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
	open.put(start)
	result = list()

	while not open.empty():
		x:Node = open.get()

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
		sub = x.subNode(goal,matrix)
		for i in sub:
			if not close.is_contains(i):
				open.put(i)

		print("Danh sach cac node trong Priority Queue")
		for item in list(open.queue):
			print("\t({0},{1}): f = {2}, g = {3}, stt = {4}".format(item.x,item.y,item.f,item.g,item.stt))
	return result



