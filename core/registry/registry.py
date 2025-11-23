class _Registry():
    def __init__(self):
        self.models = {}

    def register(self, cls):
        if self.models.get(cls._name):
            raise ValueError("Registry is a set, duplicated entry: " + cls._name)
        self.models[cls._name] = cls
        return True
    
    def __str__(self):
        return f'Registry({len(self.models)} modules): {str(self.models)}'


registry = _Registry()