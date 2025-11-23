class _Registry():
    def __init__(self):
        self.models = {}

    def register(self, cls):
        if self.models.get(cls._name):
            raise ValueError("Registry is a set, duplicated entry: " + cls._name)
        self.models[cls._name] = cls
        return True
    
    def __str__(self):
        to_ret = f'Registry ({len(self.models)} modules):\n' + "{\n"
        for record in self.models:
            to_ret += f'\t{record}: {self.models.get(record)}\n'
        to_ret += "}"
        return to_ret


registry = _Registry()
