# simple_kuramoto_demo.py
# A minimal Kuramoto model to illustrate phase synchronization (DRAI-style core)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of oscillators
N = 10

# Coupling strength
K = 0.5

# Time settings
dt = 0.05
T = 50
steps = int(T / dt)

# Initialize phases randomly (0 to 2pi)
theta = np.random.uniform(0, 2 * np.pi, N)

# Natural frequencies (slightly varied)
omega = np.random.normal(1.0, 0.1, N)

# For plotting
history = np.zeros((steps, N))

def kuramoto_step(theta, omega, K):
    """Single update step for Kuramoto oscillators"""
    dtheta = np.zeros_like(theta)
    for i in range(N):
        interaction = np.sum(np.sin(theta - theta[i]))
        dtheta[i] = omega[i] + (K / N) * interaction
    return theta + dtheta * dt

# Simulate
for t in range(steps):
    theta = kuramoto_step(theta, omega, K)
    history[t] = theta % (2 * np.pi)  # Keep in [0, 2pi]

# Plotting animation
fig, ax = plt.subplots()
lines = [ax.plot([], [], label=f'Osc {i}')[0] for i in range(N)]
ax.set_xlim(0, T)
ax.set_ylim(0, 2 * np.pi)
ax.set_ylabel('Phase')
ax.set_xlabel('Time')
ax.set_title('Kuramoto Synchronization (DRAI Core Demo)')

def update(frame):
    t = frame * dt
    for i, line in enumerate(lines):
        line.set_data(np.linspace(0, t, frame), history[:frame, i])
    return lines

ani = FuncAnimation(fig, update, frames=steps, blit=True, interval=20)
plt.legend()
plt.tight_layout()
plt.show()
