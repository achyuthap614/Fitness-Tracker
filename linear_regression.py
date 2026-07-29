
from typing import List, Tuple
import math
import matplotlib.pyplot as plt


class LinearRegression:
    """Simple univariate linear regression (y = a*x + b).

    Methods:
    - fit(X, y): fits slope `a` and intercept `b`.
    - predict(X): returns list of predictions for X.
    - mse(y_true, y_pred): mean squared error.
    - plot_regression(X, y, y_pred, filename=None): plots actual vs predicted and regression line.
    """

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.fitted = False

    def fit(self, X: List[float], y: List[float]):
        if len(X) != len(y) or len(X) == 0:
            raise ValueError("X and y must have same non-zero length")

        n = len(X)
        mean_x = sum(X) / n
        mean_y = sum(y) / n

        num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(X, y))
        den = sum((xi - mean_x) ** 2 for xi in X)

        if den == 0:
            # All X equal -> slope 0
            self.a = 0.0
            self.b = mean_y
        else:
            self.a = num / den
            self.b = mean_y - self.a * mean_x

        self.fitted = True
        return self.a, self.b

    def predict(self, X: List[float]) -> List[float]:
        if not self.fitted:
            raise RuntimeError("Model is not fitted yet. Call fit() first.")
        return [self.a * xi + self.b for xi in X]

    @staticmethod
    def mse(y_true: List[float], y_pred: List[float]) -> float:
        if len(y_true) != len(y_pred) or len(y_true) == 0:
            raise ValueError("y_true and y_pred must have same non-zero length")
        n = len(y_true)
        return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n

    @staticmethod
    def plot_regression(X: List[float], y: List[float], y_pred: List[float], filename: str = None):
        plt.figure(figsize=(8, 5))
        plt.scatter(X, y, color="blue", label="Actual")
        # Plot regression line sorted by X for a clean line
        xs_sorted = sorted(zip(X, y_pred), key=lambda t: t[0])
        xs = [t[0] for t in xs_sorted]
        ys = [t[1] for t in xs_sorted]
        plt.plot(xs, ys, color="red", label="Predicted (regression)")
        plt.xlabel("Steps walked")
        plt.ylabel("Calories burnt")
        plt.title("Actual vs Predicted (Linear Regression)")
        plt.legend()
        plt.tight_layout()
        if filename:
            plt.savefig(filename)
        plt.show()

      