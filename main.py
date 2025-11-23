from core.registry.registry import registry

if __name__ == "__main__":
    from models.test_model import *
    from neurons.test_neuron import *

    for i in range(10):
        test_n = TestNeuron()
    print(registry)
    print(registry.models.get('test.model')._neurons)
    print(registry.models.get('test.model.2')._neurons)
