
class DataReader:
	def __init__(self):
		self.train_data = dict()
		self.test_data = dict()
		for i in range(10):
			self.train_data[str(i)] = list()
			self.test_data[str(i)] = list()
		self.read()	


	def read(self):
		# reading train
		file = open('../optdigits-orig_train.txt', 'r')
		for i in range(2436):
			temp = list()
			for j in range(32):
				cur = file.readline()
				cur = cur[0:32]
				temp.append(cur)
			cur = file.readline()
			self.train_data[cur[1]].append(temp)
		file.close()
		
		# reading test
		file = open('../optdigits-orig_test.txt', 'r')
		for i in range(444):
			temp = list()
			for j in range(32):
				cur = file.readline()
				cur = cur[0:32]
				temp.append(cur)
			cur = file.readline()
			self.test_data[cur[1]].append(temp)
		file.close()
		# for i in range(10):
		# 	for j in self.test_data[str(i)]:
		# 		for k in j:
		# 			print(k)
		# 	print()

a = DataReader()