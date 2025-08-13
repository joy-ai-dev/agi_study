import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Data setup
X = np.array([[1], [2], [3]])
y = np.array([[2], [4], [6]])
w = np.array([[1.0]])  # start with weight = 1.0

plt.ion()  # Interactive mode on
fig, ax = plt.subplots(figsize=(8, 6))

def clear_ax():
    ax.clear()
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 8)
    ax.axis('off')

def draw_title(text):
    ax.text(2, 7.5, text, fontsize=16, fontweight='bold', ha='center')

def draw_step(text_lines, ypos=6):
    for i, line in enumerate(text_lines):
        ax.text(0.1, ypos - i*0.6, line, fontsize=12, ha='left')

def draw_diagram(X_val=None, w_val=None, y_pred=None, y_true=None):
    # Draw boxes and arrows representing data flow
    
    # Input box
    rect_x = patches.Rectangle((0.3, 4.5), 1.2, 1, fill=True, edgecolor='black', linewidth=1, facecolor='lightblue')
    ax.add_patch(rect_x)
    ax.text(0.9, 5, 'Input X', fontsize=12, ha='center', va='center')
    if X_val is not None:
        ax.text(0.9, 4.7, f'{X_val.flatten().tolist()}', fontsize=10, ha='center', va='center')
    
    # Weight box
    rect_w = patches.Rectangle((2, 4.5), 1.2, 1, fill=True, edgecolor='black', linewidth=1, facecolor='lightgreen')
    ax.add_patch(rect_w)
    ax.text(2.6, 5, 'Weight w', fontsize=12, ha='center', va='center')
    if w_val is not None:
        ax.text(2.6, 4.7, f'{w_val.flatten()[0]:.2f}', fontsize=10, ha='center', va='center')
    
    # Output box
    rect_yhat = patches.Rectangle((3.5, 4.5), 1.2, 1, fill=True, edgecolor='black', linewidth=1, facecolor='salmon')
    ax.add_patch(rect_yhat)
    ax.text(4.1, 5, 'Prediction ŷ', fontsize=12, ha='center', va='center')
    if y_pred is not None:
        ax.text(4.1, 4.7, f'{y_pred.flatten().round(2).tolist()}', fontsize=10, ha='center', va='center')
    
    # Arrow X -> w
    ax.annotate('', xy=(2, 5), xytext=(1.5, 5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    # Arrow w -> ŷ
    ax.annotate('', xy=(3.5, 5), xytext=(3.2, 5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

def draw_error(y_true, y_pred):
    # Show error calculation below
    ax.text(0.1, 3.5, "Error = y - ŷ", fontsize=14, fontweight='bold')
    ax.text(0.1, 3.0, f"Error = {y_true.flatten().tolist()} - {y_pred.flatten().round(2).tolist()} =", fontsize=12)
    error = y_true - y_pred
    ax.text(0.1, 2.5, f"{error.flatten().round(2).tolist()}", fontsize=12, color='red')

def draw_update(w, grad, lr=0.1):
    ax.text(0.1, 1.5, "Weight Update Rule:", fontsize=14, fontweight='bold')
    ax.text(0.1, 1.1, r"$w \leftarrow w + \eta \times \frac{X^T \cdot error}{n}$", fontsize=16)
    ax.text(0.1, 0.7, f"Current w = {w.flatten()[0]:.4f}", fontsize=12)
    ax.text(0.1, 0.3, f"Gradient = {grad.flatten()[0]:.4f}", fontsize=12, color='blue')
    new_w = w + lr * grad
    ax.text(0.1, -0.1, f"New w = {new_w.flatten()[0]:.4f}", fontsize=12, color='green')
    return new_w

# Animate step-by-step

for step in range(3):
    clear_ax()
    if step == 0:
        draw_title("Step 1: Calculate Prediction ŷ")
        draw_step([
            "ŷ = X × w",
            "X = [1, 2, 3]",
            "w = 1.00 (initial weight)"
        ])
        y_pred = X * w
        draw_diagram(X, w, y_pred)
    elif step == 1:
        draw_title("Step 2: Calculate Error")
        draw_step([
            "Error = y - ŷ",
            "y = [2, 4, 6]",
            f"ŷ = {y_pred.flatten().round(2).tolist()}"
        ])
        draw_diagram(X, w, y_pred)
        draw_error(y, y_pred)
    elif step == 2:
        draw_title("Step 3: Update Weight")
        error = y - y_pred
        grad = (X.T @ error) / len(X)
        draw_diagram(X, w, y_pred)
        new_w = draw_update(w, grad, lr=0.1)
        w = new_w

    plt.pause(4)

# Final prediction with updated weight
clear_ax()
draw_title("Final Prediction with Updated Weight")
draw_step([
    f"New weight w = {w.flatten()[0]:.4f}",
    "Calculate ŷ = X × w"
])
y_pred = X @ w
draw_diagram(X, w, y_pred)
ax.text(0.1, 3.5, f"ŷ = {y_pred.flatten().round(2).tolist()}", fontsize=14, color='green')

plt.pause(5)

plt.ioff()
plt.show()
