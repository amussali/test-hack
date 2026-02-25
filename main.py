import numpy as np


def main():
    print("Hello from new-folder!")


class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        # Xavier initialization for weights
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(1.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(1.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_deriv(self, x):
        s = self.sigmoid(x)
        return s * (1 - s)

    def relu(self, x):
        return np.maximum(0, x)

    def relu_deriv(self, x):
        return (x > 0).astype(float)

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, lr=0.01):
        m = X.shape[0]
        y_pred = self.a2
        # Binary cross-entropy loss gradient
        dz2 = y_pred - y
        dW2 = self.a1.T @ dz2 / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m

        da1 = dz2 @ self.W2.T
        dz1 = da1 * self.relu_deriv(self.z1)
        dW1 = X.T @ dz1 / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m

        # Update parameters
        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1

    def train(self, X, y, epochs=1000, lr=0.01, print_loss=False):
        for i in range(epochs):
            y_pred = self.forward(X)
            self.backward(X, y, lr)
            if print_loss and i % (epochs // 10) == 0:
                loss = -np.mean(
                    y * np.log(y_pred + 1e-8) + (1 - y) * np.log(1 - y_pred + 1e-8)
                )
                print(f"Epoch {i}, Loss: {loss:.4f}")

    def predict(self, X):
        preds = self.forward(X)
        return (preds > 0.5).astype(int)


if __name__ == "__main__":
    main()
