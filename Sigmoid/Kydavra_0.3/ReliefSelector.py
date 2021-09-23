# Importing all needed libraries
import numpy as np


class ReliefSelector:

    """
    |============================================|
    | n <-- number of training instances         |
    | a <-- number of attributes (i.e. features) |
    |============================================|
    """

    def __init__(self, n_neighbors, n_features_to_keep):
        self.n_neighbors = n_neighbors
        self.n_features_to_keep = n_features_to_keep

    """
    |======================================================================================|
    |Scikit-learn required: Computes the feature importance scores from the training data. |
    |Parameters                                                                            |
    |                                                                                      |
    |X: array-like {n_samples, n_features}                                                 |
    |    Training instances to compute the feature importance scores from                  |
    |y: array-like {n_samples}                                                             |
    |    Training labels                                                                   |
    |weights: parameter for iterative relief                                               |
    |Returns                                                                               |
    |                                                                                      |
    |Copy of the ReliefF instance                                                          |
    |======================================================================================|
    """

    def fit(self, X, y):

        # pre-compute distance array
        # distance = euclidean_distances(X, X)
        distance = pairwise_distances(X, metric='manhattan')

        # initialize all feature weights := 0.0
        score = np.zeros(X.shape[1])

        # the number of classes
        c = np.unique(y).tolist()

        for i in range(X.shape[0]):

            nearest_hits = []
            nearest_misses = []

            for j in range(X.shape[0]):
                # identify k nearest hits and k nearest misses (using distance array)
                pass
