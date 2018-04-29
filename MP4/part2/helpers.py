import numpy as np

def Affine_Forward(A,W,b):
	n,d,d_p = len(A), len(W[0]), len(W)
	Z = np.zeros((n,d))
	for i in range(n):
		for j in range(d):
			for k in range(d_p):
				Z[i][j] += A[i][k]*W[k][j]
			Z[i][j] += b[j]
	return Z


def ReLu_Forward(Z):
	r,c = Z.shape
	for i in range(r):
		for j in range(c):
			reLu = max(0, Z[i][j])
			Z[i][j] =reLu
	return Z






