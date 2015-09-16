from numpy import array, zeros, exp, linspace
from time import time

n = array([10, 100, 1000, 10000])
T_coeffs = []

for N in n:
	dx = 1.0/(N - 1)

	x = linspace(0.0, 1.0, N + 2)
	g = (dx**2*(100.0*exp(-10.0*x)))[1:-1]

	a = zeros(N) - 1.0
	b = zeros(N) + 2.0
	c = zeros(N) - 1.0

	r = zeros(N)
	s = zeros(N)

	v = zeros(N)

	start = time();

	r[0] = g[0]/b[0]
	s[0] = -c[0]/b[0]
	for i in xrange(1, N - 1):
		r[i] = (g[i] - a[i]*r[i - 1])/(a[i]*s[i - 1] + b[i])
		s[i] = -c[i]/(a[i]*s[i - 1] + b[i])
	r[N - 1] = (g[N - 1] - a[N - 1]*r[N - 1])/(a[N - 1]*s[N - 2] + b[N - 1]);
	v[N - 1] = r[N - 1]
	i = N - 1
	while i > 0:
		v[i - 1] = r[i - 1] + s[i - 1]*v[i]
		i -= 1

	finish = time();
	T_coeffs += [finish - start]

for i in xrange(5):
	print n[i], "\t", T_coeffs[i]

# N	T
# 10 	0.000297069549561
# 100 	0.00283002853394
# 1000 	0.0281019210815
# 10000 0.278719902039
