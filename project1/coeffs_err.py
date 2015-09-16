from numpy import array, zeros, exp, linspace, log
from matplotlib.pyplot import plot, show, hold, axis, title, xlabel, ylabel, figure, legend

n = array([10, 100, 1000, 10000, 100000])
e = []

for N in n:
	h = 1.0/(N - 1)

	x = linspace(0.0, 1.0, N + 2)
	g = (h**2*(100.0*exp(-10.0*x)))[1:-1]

	a = zeros(N) - 1.0
	b = zeros(N) + 2.0
	c = zeros(N) - 1.0

	r = zeros(N)
	s = zeros(N)

	v = zeros(N)

	r[0] = g[0]/b[0]
	s[0] = -c[0]/b[0]
	for i in xrange(1, N):
		r[i] = (g[i] - a[i]*r[i - 1])/(a[i]*s[i - 1] + b[i])
		s[i] = -c[i]/(a[i]*s[i - 1] + b[i])
	v[N - 1] = r[N - 1]
	i = N - 1
	while i > 0:
		v[i - 1] = r[i - 1] + s[i - 1]*v[i]
		i -= 1

	u = (1.0 - (1.0 - exp(-10.0))*x - exp(-10.0*x))[1:-1]

	errors = log(abs((v - u)/u))/log(10.0)
	e += [max(errors)]

plot(x[1:-1], v, 'b-')
hold('on')
plot(x[1:-1], u, 'g-')
title('Solutions of the Poisson equation ($N=10\;000$)')
xlabel('$x$')
ylabel('$u(x),\;v(x)$')
legend(['Numerical', 'Exact'])
show()

E = array(e)
plot(log(n)/log(10), E ,'-x')

axis([0, 6, -5, 0])

title("Relative error, logarithmic scale")

xlabel('N')

ylabel('Relative error $\epsilon$')
show()
