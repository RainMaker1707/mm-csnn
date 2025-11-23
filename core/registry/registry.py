class _Registry():
    def __init__(self):
        self.models = {}
        self.neurons = {}

    def register_module(self, cls):
        if self.models.get(cls._name):
            raise ValueError("Registry is a set, duplicated entry: " + cls._name)
        self.models[cls._name] = cls
        return True

    def register_neuron(self, cls):
        if self.neurons.get(cls._name):
            raise ValueError("Registry is a set, duplicated entry: " + cls._name)
        self.neurons[cls._name] = cls
        return True

    def __str__(self):
        to_ret = f'Registry ({len(self.models)} modules, {len(self.neurons)} neurons):\n' + "Modules:\n{\n"
        for record in self.models:
            to_ret += f'\t{record}: {self.models.get(record)}\n'
        to_ret += "}\nNeurons:\n{\n"
        for record in self.neurons:
            to_ret += f'\t{record}: {self.neurons.get(record)}\n'
        return to_ret


registry = _Registry()
