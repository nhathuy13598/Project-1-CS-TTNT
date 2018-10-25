from Class import ClassNode

#-------------------------------Ghi file-------------------------------------------#
def writeFile(filename,mode,data):
	try:
		with open(filename, mode) as file:
			# In do dai duong di
			file.write(int.__str__(data[0])+'\n')

			# In duong di
			for i in data[2]:
				file.write("({0},{1}) ".format(i.x,i.y))
			file.write("\n")

			# In ma tran duong di
			size = len(data[1])
			for i in range(size):
				str = ""
				for j in range(size):
					
					if (i == data[3].x) and (j == data[3].y):
						str = str + "S "
					elif i == data[4].x and j == data[4].y:
						str = str + "G "
					elif data[2].is_containt(ClassNode.Node(i,j,None)):
						str = str + "x "
					elif data[1][i][j] == 0:
						str = str + "- "
					else:
						str = str + "o "
				file.write(str+'\n')
			return True
	except EOFError:
		print("Khong the mo file ghi",filename)
		return False
#----------------------------------Kết thúc ghi file---------------------------------------#