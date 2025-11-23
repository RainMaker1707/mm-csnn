from core.meta import meta

class Module(metaclass=meta.MetaClass):
    _name = None
    _register = True
    _abstract = False
