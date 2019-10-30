from matplotlib.pyplot import figure
import numpy as np
import scipy.optimize

def plot_fit(data_x, data_y, fit_function, ax):
    ax.plot(data_x, data_y, 'o', label='data')
    popt, pcov = scipy.optimize.curve_fit(fit_function, data_x, data_y)
    x_plot = np.linspace(data_x.min(), data_x.max())
    ax.plot(x_plot, fit_function(x_plot, *popt), label='Fit')
    ax.grid()
    ax.legend()

f = figure()
X = np.linspace(-2,2, 13)
Y = 0.2*X**2 + 2*X + 0.3
Y_noise = Y + 1*(np.random.rand(len(X))-0.5)
ax1, ax2 = f.subplots(2, 1, sharex=True, sharey=True)
plot_fit(X, Y_noise, lambda x, a, b:a*x + b, ax1)
ax1.set_title("linear")
plot_fit(X, Y_noise, lambda x, a, b, c:a*x**2 + b*x +c, ax2)
ax2.set_title("quadratic")
f.tight_layout()