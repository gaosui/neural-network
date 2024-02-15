from layer import Layer

class Network:
    def __init__(self, layers: list[Layer]) -> None:
        self.layers = layers

    def train(self, x, num_iterations):
        for i in range(num_iterations):
            self._train_once(x)

    def _forward_all(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def _train_once(self, x):
        out = self._forward_all(x)
        # compute J from out
        # compute dJ/da
        # print/plot J

        da = ...
        for layer in reversed(self.layers):
            da = layer.backward(da)

    def predict(self, input):
        out = self._forward_all(input)

        # Sample from out
        