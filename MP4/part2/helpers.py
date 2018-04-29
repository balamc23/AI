import numpy as np

def Affine_Forward(A,W,b):
	cache = (A,W,b)
	n,d,d_p = len(A), len(W[0]), len(W)
	Z = np.zeros((n,d))
	for i in range(n):
		for j in range(d):
			for k in range(d_p):
				Z[i][j] += A[i][k]*W[k][j]
			Z[i][j] += b[j]
	return Z,cache


def ReLu_Forward(Z):
	cache = Z
	r,c = Z.shape
	for i in range(r):
		for j in range(c):
			reLu = max(0, Z[i][j])
			Z[i][j] =reLu
	return Z,cache

def Affine_Backward(dZ, cache):
	A,W = cache[0],cache[1]
	I,K,J = len(dZ), len(W), len(W[0])
	dA,dW,db = np.zeros((I,J)), np.zeros((K,J)), np.zeros(J)
	for i in range (I):
		for k in range(K):
			for j in range(J):
				dA[i][k] += dZ[i][j]*W[k][j]

	for k in range(K):
		for j in range(J):
			for i in range(I):
				dw[k][j] += A[i][k]*dZ[i][j]

	for j in range(J):
		for i in ragne(I):
			db[j] += dZ[i][j]

	return dA,dW,db


def ReLu_Backward(dA, cache):
	dZ = dA
	r,c = dA.shape
	for i in range(r):
		for j in range(c):
			reLu = max(0, dA[i][j])
			dZ[i][j] = reLu	

	return dZ


def Cross_Entropy(F,y,n):
	I,J,C = len(F), len(F[0]), 3
	dF = np.zeros((I,J))
	loss =0
	for i in range(I):
		Y = y[i]
		middle_sum = 0
		for k in range(C):
			middle_sum += np.exp(F[i][k])

		middle_sum = np.log(middle_sum)
		loss += F[i][Y] - middle_sum
	loss = (-1/n)*loss

	for i in range(I):
		for j in range(J):
			denom = 0 
			for k in range(C):
				denom += np.exp(F[i][k])
			indicator = 0
			if(j == y[i]):
				indicator = 1 
			dF[i][j] = (-1/n) *(indicator - np.exp(F[i][j])/denom)

	return loss, dF




