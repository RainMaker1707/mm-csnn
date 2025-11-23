# mm-csnn
MM-cSNN: Multi-Modular - continuous-time Spike Neural Network

The idea behind cSNN is to stick to the biological evolution of brains. Brains use continuous spike to transfer and treat information and data through neural connection. Neurons are for most binary and only spike to all their output neighbor if some threshold is trespassed in their input neighbor.

## Meta-Classes
### Modules
A module is a meta-class defined in core/module/. 
By default any inherited class of module.Module are registered in the core.registry.
Three attributes can be used to defined a module.
- _name: **mandatory** attribute defining the name of the module and its key in the registry
- _register: **optional** attribute defining if the module should be register in the registry. By default set as True, can be override in the inherited class to avoid registering. If you want to define an abstract class which you don't want to be register please use the argument _abstract to keep it readable.
- _abstract: **optional** attribute defining an abstract module which is not wanted to be registered. By default set as False, can be override in the inherited class to avoid registering. It it te inverse of the _register attribute.

The check for registry is defined as follow:
```py
if not _registered or _abstract:
    #do not register
    return new_cls
```
In the case of _registered set as True and _abstract set as True too, the default behavior is to not register the abstract classes.

## Registry
