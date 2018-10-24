from Class.ClassMatrix import matrix

# Mở file
def openfile(filename, mode):  
	try:
		with open(filename, mode):
			return open(filename, 'r')
	except IOError:
		print ("Could not read file:", filename)
		return False

# Đọc file
def readfile(filename):
	file = openfile(filename,"r")
	if file != False: 

		#sizeOfMatrix
		size = int(file.readline())

		#read start point
		a = file.readline()
		start = (int(a[:a.find(" ")]), int(a[a.find(" "):]))

		#read goal point
		a = file.readline()
		goal = (int(a[:a.find(" ")]), int(a[a.find(" "):]))

		#read matrix
		data = []
		for i in range(size):
			data.append([])
			d = file.readline()
			a = b = 0
			while (b < len(d)):
				if d[b] == " ":
					data[i].append(int(d[a:b]))
					a = b
				b += 1
			data[i].append(int(d[a:]))
		file.close()
		return (matrix(size,data),start,goal)
	else:
		return False