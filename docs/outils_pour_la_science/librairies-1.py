from matplotlib.pyplot import figure
from numpy import linspace
from sympy import Symbol, cos, sqrt, diff, lambdify

x = Symbol('x')
f = cos(sqrt(1+x**2))**5
f_seconde = diff(f, x, x)
f_seconde_numpy = lambdify(x, f_seconde, 'numpy')


X = linspace(-np.pi/2, np.pi/2, 100)
Y = f_seconde_numpy(X)
fig = figure(figsize=(6, 3))
ax = fig.subplots(1, 1)
ax.plot(X,Y)
ax.set_title('Derivée seconde de {}'.format(f))