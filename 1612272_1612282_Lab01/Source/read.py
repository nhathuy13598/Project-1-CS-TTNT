
# Mở file
def openfile(filename, mode) -> tuple:  
	try:
		with open(filename, mode) as file:
			#sizeOfMatrix
			size = int(file.readline())
		
			#read start point
			a = file.readline()
			start = tuple(map(int,a.split()))

			#read goal point
			a = file.readline()
			goal = tuple(map(int,a.split()))

			#read matrix
			data = []
			for _ in range(size):
				d = file.readline()
				data.append(list(map(int,d.split())))
				
			return (data,start,goal)
	except IOError:
		print ("Could not read file:", filename)
		return False