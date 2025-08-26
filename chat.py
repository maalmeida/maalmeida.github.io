import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate the solution line
t = np.linspace(-2, 2, 100)
x1 = 1 - t
x2 = -1 - 2*t
x3 = 4 - 3*t
x4 = t  # 4th dimension

# Normalize x4 for colormap
norm = plt.Normalize(x4.min(), x4.max())
colors = plt.cm.viridis(norm(x4))

# Setup figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    ax.scatter(x1, x2, x3, c=x4, cmap='viridis', s=10)
    ax.scatter(1, -1, 4, color='red', s=50, label='Particular Solution')
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$x_3$')
    ax.set_title('4D Solution Line (Rotating View)')
    ax.view_init(elev=20, azim=frame)
    ax.legend()
    return ax,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 60), interval=100)

# Save or show
# Uncomment the following line to save as .mp4 (requires ffmpeg)
# ani.save('solution_line_4d_rotation.mp4', writer='ffmpeg', fps=30)

plt.show()
