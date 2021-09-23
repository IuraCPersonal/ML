import numpy as np
import pandas as pd


class FisherSelector:

    def __init__(self, n_features, gamma):
        self.n_features = n_features
        self.gamma = gamma

    def generate_p_set(self, X):
        A = np.arange(2**X.shape[1])
        a = np.asarray(A, dtype=np.uint8).reshape(len(A), 1)
        B = np.unpackbits(a, axis=1)
        b = [row for row in B if row.sum() == self.n_features]
        return b

    def get_k(self, X, j):
        return np.dot(X[:, j].T, X[:, j])

    def get_v(self, X, lambda_vector, p_set):
        temp = 0

        for i in range(X.shape[1]):
            temp += p_set[i] * self.get_K(X, i)

        V = 1/self.gamma * temp * lambda_vector.sum()

        print(np.linalg.pinv(np.diagflat(V)))


    def select(self, df, target):
        X = df.drop(target, axis=1).values
        y = df[target].values

        n = X.shape[0]
        c = len(np.unique(y))

        p_set = self.generate_p_set(X)
        lambda_vector = np.random.normal((1, len(p_set)))

        Ic = np.zeros((n, n))
        Ic[:c, :c] = np.identity(c).T

        V = 1/n * np.dot(np.identity(n), Ic)

        p_max = 0
        p_index = 0

        for i in range(len(p_set)):
            p_sum = 0
            for j in range(X.shape[1]):
                p_sum += p_set[i][j] * np.linalg.multi_dot([X[:, j], V, V.T, X[:, j].T])
            if p_max < p_sum:
                p_max = p_sum
                p_index = i

        theta = p_max
        omega = set(tuple(p_set[p_index]))

        # Debugging:
        self.get_v(X, lambda_vector, p_set)

df = pd.read_csv('heart.csv')

test = FisherSelector(4, 5)
test.select(df, "target")