from numpy import array, zeros, exp, linspace, log
from scipy.linalg import lu_factor, lu_solve
from time import time

n = array([10, 100, 1000, 10000])
T = []

for N in n:d
	h = 1.0/(N - 1)

	x = linspace(0.0, 1.0, N + 2)
	g = (h**2*(100.0*exp(-10.0*x)))[1:-1]
	A = zeros((N, N))

	for i in xrange(N): A[i, i] = 2.0
	for i in xrange(1, N - 1):
		A[i - 1, i] = -1.0
		A[i, i - 1] = -1.0

	start = time()


	LU, P = lu_factor(A)
	v = lu_solve((LU, P), g)

	finish = time()

	T += [finish - start]

for i in xrange(4):
	print n[i], "\t", T[i]


# N	T
# 10 	0.000398874282837
# 100 	0.0012321472168
# 1000 	0.285443067551
# 10000 57.1268138885
