class files:
	def read_write(self):
		try:
			file = input("Enter the file name : ")
			f = open(file,"r+")
		except Exception as e:
			print(e)

