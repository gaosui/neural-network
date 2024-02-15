from network import Network
from layer import Layer
import activation

net = Network([
    Layer(10, 28 * 28, activation.Sigmoid),
    Layer(10, 10, activation.Softmax)
])
net.train()

# Test..