import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([[1],[2],[3]])
y = np.array([[2],[4],[6]])

# Weight
w = np.random.rand(1,1)

plt.ion()  # interactive mode on
fig, ax = plt.subplots()

# Show empty plot first
ax.set_title("Waiting to start animation...")
ax.scatter([], [])  # empty plot points
plt.show(block=False)  # show non-blocking plot window


for step in range(1000):
    pred = X @ w
    error = y - pred
    w += 0.01 * (X.T @ error) / len(X)

    ax.clear()
    ax.scatter(X, y, color='blue', label='Data')
    ax.plot(X, pred, color='red', label='Prediction')
    ax.set_title(f"Step {step+1} — w={w[0][0]:.2f}")
    ax.legend()
    plt.pause(0.1)

plt.ioff()
plt.show()