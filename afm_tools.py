import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_afm_csv(file):
    data = pd.read_csv(file, header=None)
    return data

def plot_afm_surface(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(range(data.shape[1]), range(data.shape[0]))
    Z = data.values
    ax.plot_surface(X, Y, Z, cmap='viridis')
    return fig

def compute_stats(data):
    Z = data.values
    avg_height = np.mean(Z)
    roughness = np.std(Z)
    return avg_height, roughness
