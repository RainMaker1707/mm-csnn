from typing import Dict

from core.meta import module_meta as meta


class Module(metaclass=meta.ModuleMeta):
    _name = None
    _register = True
    _abstract = False
    # Need override in subclass to dissociate neurons list
    _neurons: Dict[int, 'Neuron'] = None

    @classmethod
    def add_neuron(cls, neuron_id, neuron):
        if cls._neurons.get(neuron_id):
            raise ValueError(f'Neuron {neuron_id} already registered in module {self._name}')
        cls._neurons[neuron_id] = neuron
        return True
