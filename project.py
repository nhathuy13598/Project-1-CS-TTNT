import math
import sys
import ThuatToan
import read
import write
from Class.ClassNode import Node
from Class.ClassMyList import mylist
from queue import PriorityQueue


# Hàm main
def main():
	if(len(sys.argv) == 3):
		file = read.readfile(sys.argv[1])
		if not file: 
			print("Error!!!")
			return
		start = Node(file[1][0],file[1][1],None)
		goal = Node(file[2][0],file[2][1],None)
		matrix = file[0]
		result = mylist(ThuatToan.A(start,goal,matrix))
		f = write.writeFile(sys.argv[2],"w", (len(result),matrix,result,start,goal))
		if not f:
			print("Error!!!")
	else:
		print("Error!!!")
main()