from core.module import module


class TestModel(module.Module):
    _name = "test.model"
    _register = True


class TestModel2(module.Module):
    _name = "test.model.2"
    _register = True


class TestNotRegistered(module.Module):
    _name = "test.model.not.registered"
    _register = False