from core.models.neuron import Neuron


class TestNeuron(Neuron):
    _name = "test.neuron"
    _register = True

    def __init__(self):
        super().__init__('test.model')


class TestNeuron2(Neuron):
    _name = "test.neuron.2"
    _register = True


class TestNotRegisteredNeuron(Neuron):
    _name = "test.neuron.not.registered"
    _register = False


class TestAbstractNeuron(Neuron):
    _name = "test.abstract.neuron"
    _abstract = True
