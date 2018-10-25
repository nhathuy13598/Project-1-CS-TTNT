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

		# Doc file - return tuple(data,start,goal)
		file = read.openfile(sys.argv[1],"r")

		# Lay ma tran
		matrix = file[0]

		# Lay nut start
		start = Node(file[1][0],file[1][1],None)

		# Lay nut goal
		goal = Node(file[2][0],file[2][1],None)
		if goal.check(matrix) == False:
			print("Diem goal la diem khong di duoc")
			print("Complete!!!")
			return

		# Giai bai toan
		result = mylist(ThuatToan.A(start,goal,matrix))

		# In ra loi giai
		if len(result) != 0:
			write.writeFile(sys.argv[2],"w", (len(result),matrix,result,start,goal))
		else:
			print("Khong tim ra loi giai")
	else:
		print("Thieu tham so dau vao")

	# Kiem tra chuong trinh chay dung hay khong
	print("Complete!!!")
main()