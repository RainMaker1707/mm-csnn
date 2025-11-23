from typing import Dict

from core.models.module import Module


class TestModel(Module):
    _name = "test.model"
    _register = True
    _neurons: Dict[int, 'Neuron'] = {}


class TestModel2(Module):
    _name = "test.model.2"
    _register = True
    _neurons: Dict[int, 'Neuron'] = {}


class TestNotRegistered(Module):
    _name = "test.model.not.registered"
    _register = False
    _neurons: Dict[int, 'Neuron'] = {}


class TestAbstractModule(Module):
    _name = "test.abstract.module"
    _abstract = True