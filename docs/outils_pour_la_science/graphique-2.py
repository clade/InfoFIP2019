from matplotlib.pyplot import figure
import numpy as np
X = np.linspace(-2,2, 100)
Y = np.sin(X)**2*np.exp(-X**2)
Y_noise = Y + .1*(np.random.rand(len(X))-0.5)
f = figure(figsize=(5,3)) # The size can be specified
ax = f.subplots(1, 1)
ax.plot(X, Y, label=u"Theory")
ax.plot(X, Y_noise,'o', label=u"Experiment")
ax.set_xlabel(u'Voltage [V]')
ax.set_ylabel(u'Length [m]')
ax.set_title("Nonsense graph with object!")
ax.legend()
ax.grid(True)
f.tight_layout()