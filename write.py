from Class import ClassNode

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
				elif data[2].is_containt(ClassNode.Node(i,j,None)):
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