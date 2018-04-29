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


	return dA,dW,db


def ReLu_Backward(dA, cache):
	dZ = dA
	r,c = dA.shape
	for i in range(r):
		for j in range(c):
			reLu = max(0, dA[i][j])
			dZ[i][j] = reLu	

	return dZ





