from core.meta import neuron_meta as meta
from core.registry.registry import registry
from core.models.synapse import Synapse


class Neuron(metaclass=meta.NeuronMeta):
    __next_id: int = 1
    
    _name: str = None
    _register: bool = True
    _abstract: bool = False

    def __init__(self, module, threshold=0.3):
        self.module = module
        self.threshold = threshold
        self.id = Neuron.__next_id
        self.synapse = Synapse(self)
        Neuron.__next_id +=1
        model = registry.models.get(module)
        if not model:
            raise ValueError(f'The module {module} doesn\'t exist in the registry:\n' + str(registry))
        model.add_neuron(self.id, self)

    def add_output(self, output):
        self.synapse.add(output)

    def remove_output(self, output):
        self.synapse.remove(output)
