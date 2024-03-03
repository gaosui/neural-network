import numpy as np

class Sigmoid:
    def call(self, x):
        sigma_x = 1 / (1 + np.exp(-x))
        return sigma_x

    def derivative(self, x):
        sigma_x = self.call(x)
        d_sigma_x = sigma_x * (1 - sigma_x)
        return d_sigma_x

class Softmax:
    def call(self, x):
        exp_x = np.exp(x)
        softmax_x = exp_x / np.sum(exp_x, axis=0)
        return softmax_x

    def derivative(self, input):

        pass
