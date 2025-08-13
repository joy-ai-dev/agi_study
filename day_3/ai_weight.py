import numpy as np

# Training data
X = np.array([[1], [2], [3]])
y = np.array([[2], [4], [6]])  

w = np.random.rand(1, 1)  # weight
for _ in range(1000):  # train 1000 times
    pred = X * w
    error = y - pred
    w += 0.01 * (X.T @ error) / len(X)  # gradient descent step

print("Learned weight:", w)
print("Predict 4 →", np.array([[4]]) @ w)