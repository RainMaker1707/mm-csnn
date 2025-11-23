from core.registry.registry import registry


class MetaClass(type):
    def __new__(self, name, bases, attrs):
        new_cls = super().__new__(self, name, bases, attrs)
        if name == "Module":
            return new_cls
        _name = getattr(new_cls, "_name", None)
        _register = getattr(new_cls, "_register", True)
        _abstract = getattr(new_cls, "_abstract", False)

        if not _register or _abstract:
            return new_cls
        
        if _name is None:
            raise TypeError(f'Module {name} must define _name field')
        
        if registry.models.get(_name):
            raise ValueError(f'Duplicated module: {_name}')
        
        registry.register(new_cls)
        return new_cls
