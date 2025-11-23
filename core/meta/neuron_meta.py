from core.registry.registry import registry


class NeuronMeta(type):
    def __new__(self, name, bases, attrs):
        new_cls = super().__new__(self, name, bases, attrs)

        if name == "Neuron":
            return new_cls

        _name = getattr(new_cls, "_name", None)
        _register = getattr(new_cls, "_register", True)
        _abstract = getattr(new_cls, "_abstract", False)

        if not _register or _abstract:
            return new_cls

        if _name is None:
            raise TypeError(f'Neuron {name} must define _name field')

        registry.register_neuron(new_cls)
        return new_cls
