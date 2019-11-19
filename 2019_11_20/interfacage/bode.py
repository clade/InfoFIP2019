import inspect
from numpy import sin, pi, arange
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit


def my_curve_fit(f, xdata, ydata, p0={}):
    name_of_parameters = inspect.getfullargspec(f).args[1:]
    default_value = inspect.getfullargspec(f).defaults
    initial_param = {name:val for name,val in zip(name_of_parameters, default_value)}
    initial_param.update(p0)
    p0_list = [initial_param[name] for name in name_of_parameters]
    p_cov, _ = curve_fit(f, xdata, ydata, p0_list)
    return {name:p_cov[i] for i, name in enumerate(name_of_parameters)}


def fonction_sinus(t, offset=0, amplitude=1, phase=0, frequence=100):
    return offset + amplitude*np.sin(2*np.pi*frequence*t + phase)

class FitSinus(object):
    def __init__(self, temps, signal, frequence):
        self.temps = temps
        self.signal = signal
        p_ini = {}
        p_ini["freq"] = frequence
        p_ini["amplitude"] = (signal.max() - signal.min())/2
        p_ini["offset"] = signal.mean()
        popt = my_curve_fit(fonction_sinus, temps, signal, p_ini)
        self.popt = popt
        self.amplitude = popt['amplitude']
        self.phase = popt['phase']
        if self.amplitude<0:
            self.amplitude, self.phase = -self.amplitude, (self.phase + np.pi)%(2*np.pi)

    def plot(self):
        plt.plot(self.temps, self.signal, 'o')
        t = np.linspace(self.temps.min(), self.temps.max(), 100)
        plt.plot(t, fonction_sinus(t, **self.popt))
        plt.xlabel("Temps")
        plt.ylabel("Amplitude")

