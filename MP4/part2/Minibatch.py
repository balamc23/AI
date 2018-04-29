import numpy as np 
import helpers as h

class DeepPong:
	def __init__(self):
		self.data = np.array((readData('expert_policy.txt')))
		self.W1 = np.random.rand((5,256))
		self.W2 = np.random.rand((256,256))
		self.W3 = np.random.rand((256,256))
		self.W4 = np.random.rand((256,3))
		self.b1. = np.zeros(256)
		self.b2. = np.zeros(256)		
		self.b3. = np.zeros(256)
		self.b4. = np.zeros(3)

	def readData(self,dataFile):
		with open(dataFile) as df:
			data = df.readlines()
		return data	

	def FourLayerNetwork(self,X,W1,W2,W3,W4,b1,b2,b3,b4,y,test,n):
		Z1,acache1 = h.Affine_Forward(X,W1,b1)
		A1,rcache1 = h.ReLu_Forward(Z1)
		Z2,acache2 = h.Affine_Forward(A1,W2,b2)
		A2,rcache2 = h.ReLu_Forward(Z2)
		Z3,acache3 = h.Affine_Forward(A2,W3,b3)
		A3,rcache3 = h.ReLu_Forward(Z3)
		F,acache4  = h.Affine_Forward(A3,W4,b4)		

		if(test == 1):
			classification = []
			return classification




	def MiniBatchGD(self,Epochs):
		# self.data = np.array(self.data)
		N = 10000
		n = 2000
		for e in range(Epochs):
			self.data = np.shuffle(self.data)
			for j in range(0,N//n):
				A = []
				y = []
				for i in range(j*n,j*n+n):				
					A.append(self.data[i][:4])
					y.append(self.data[i][5])
				A = np.array(A)
				y = np.array(y)				

				loss = FourLayerNetwork(A, self.W1, self.W2, self.W3, self.W4, self.b1, self.b2, self.b3, self.b4, y, false,n)


