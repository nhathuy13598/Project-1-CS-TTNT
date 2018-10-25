from Class import ClassNode

#-------------------------------Ghi file-------------------------------------------#
def writeFile(filename,mode,data):
	try:
		with open(filename, mode) as file:
			file.write(int.__str__(data[0])+'\n')
			for i in data[2]:
				file.write("({0},{1}) ".format(i.x,i.y))
			file.write("\n")
			for i in range(len(data[1])):
				str = ""
				for j in range(len(data[1])):
					
					if (i == data[3].x) & (j == data[3].y):
						str = str + "S "
					elif data[2].is_containt(ClassNode.Node(i,j,None)):
						str = str + "x "
					elif i == data[4].x & j == data[4].y:
						str = str + "G "
					else:
						if data[1][i][j] == 0:
							str = str + "- "
						else:
							str = str + "o "
				file.write(str+'\n')
			return True
	except EOFError:
		print("Khong the mo file ghi",filename)
		return False
#----------------------------------Kết thúc ghi file---------------------------------------#