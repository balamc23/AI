import numpy as np 
import helpers as h
from progress import printProgressBar


class DeepPong:
	def __init__(self):
		self.data = np.array((self.readData('expert_policy.txt')))
		self.W1 = np.random.rand(5,256)
		self.W2 = np.random.rand(256,256)
		self.W3 = np.random.rand(256,256)
		self.W4 = np.random.rand(256,3)
		self.b1 = np.zeros(256)
		self.b2 = np.zeros(256)		
		self.b3 = np.zeros(256)
		self.b4 = np.zeros(3)
		self.learning_rate = 0.1

	def readData(self,dataFile):
		with open(dataFile) as df:
			d_r = df.readlines()
			data = np.zeros((len(d_r), 6))
			i =0
			for line in d_r:
				string =''
				j = 0	
				for h in range(len(line)):
					if(line[h] == ' ' or line[h] == '\n'):
						data[i][j] = float(string)
						string =''
						j += 1
					else:
						string += line[h]
				i += 1
				
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

		loss, dF = h.Cross_Entropy(F, y, n)
		dA3, dW4, dB4 = h.Affine_Backward(dF, acache4)
		dZ3 = h.ReLu_Backward(dA3, rcache3)
		dA2, dW3, dB3 = h.Affine_Backward(dZ3, acache3)
		dZ2 = h.ReLu_Backward(dA2, rcache2)
		dA1, dW2, dB2 = h.Affine_Backward(dZ2, acache2)
		dZ1 = h.ReLu_Backward(dA1, rcache1)
		dX, dW1, dB1 = h.Affine_Backward(dZ1, acache1)
		
		self.W1 = self.W1 - self.learning_rate * dW1
		self.W2 = self.W2 - self.learning_rate * dW2
		self.W3 = self.W3 - self.learning_rate * dW3
		self.W4 = self.W4 - self.learning_rate * dW4

		self.b1 = self.b1 - self.learning_rate*dB1
		self.b2 = self.b2 - self.learning_rate*dB2
		self.b3 = self.b3 - self.learning_rate*dB3
		self.b4 = self.b4 - self.learning_rate*dB4
		return loss



	def MiniBatchGD(self,Epochs):
		# self.data = np.array(self.data)
		N = 10000
		n = 2000
		printProgressBar(0, Epochs, prefix = 'Training:', suffix = 'Complete', length = 50)
		for e in range(Epochs):
			np.random.shuffle(self.data)
			printProgressBar(e, Epochs, prefix = 'Training:', suffix = 'Complete', length = 50)
			for j in range(0,N//n):
				A = []
				y = []
				for i in range(j*n,j*n+n):				
					A.append(self.data[i][:5])
					y.append(self.data[i][5])
				A = np.array(A)
				y = np.array(y)			

				loss = self.FourLayerNetwork(A, self.W1, self.W2, self.W3, self.W4, self.b1, self.b2, self.b3, self.b4, y, 0,n)


DP = DeepPong()
DP.MiniBatchGD(5)
