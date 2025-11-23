class _Registry():
    def __init__(self):
        self.models = {}

    def register(self, name, cls, filepath=None):
        if self.models.get(name):
            raise ValueError("Registry is a set, duplicated entry: " + name)
        self.models[name] = {
            "cls": cls,
            "module": cls.__module__,
            "filepath": filepath or "unknown"
        }
        return True
    
    def __str__(self):
        return f'Registry({len(self.models)} modules): {str(self.models)}'


registry = _Registry()