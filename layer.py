class Layer:
    def __init__(self, height: int, width: int, activation) -> None:
        self.weights = []
        self.activation = activation

    def forward(self, input):
        pass
        # save current layer z
        # save input (layer - 1 a)
        # return self.activation.call(np.matmul(w, input) + b)

    def backward(self, da):
        # self.activation.derivative(z)
        # compute dJ/dz 
        # compute dJ/da-1 with w-old
        # compute dJ/dw with a-1
        # Update w and b
        # Return da-1
        pass
