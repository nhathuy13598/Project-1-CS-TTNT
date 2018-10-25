from Class.ClassMatrix import matrix

# Mở file
def openfile(filename, mode) -> tuple:  
	try:
		with open(filename, mode) as file:
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
			for _ in range(size):
				d = file.readline()
				data.append(list(map(int,d.split())))
				
			return (data,start,goal)
	except IOError:
		print ("Could not read file:", filename)
		return False