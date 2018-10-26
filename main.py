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
		if (goal.x < 0) or (goal.y < 0) or goal.x >= len(matrix) or goal.y >= len(matrix) or matrix[goal.x][goal.y] == 1:
			print("Diem dich bi loi")
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

	# Kiem tra chuong trinh chay het hay khong
	print("Complete!!!")

if __name__ == '__main__':
	main()