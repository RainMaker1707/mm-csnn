# mm-csnn
MM-cSNN: Multi-Modular - continuous-time Spike Neural Network

The idea behind cSNN is to stick to the biological evolution of brains. Brains use continuous spike to transfer and treat information and data through neural connection. Neurons are for most binary and only spike to all their output neighbor if some threshold is trespassed in their input neighbor.


## Registry
The registry is a singleton that keep trace of each modules and neurons types (not the instanced objects) into two separated dictionaries.
- **registry.models** is the dictionary keeping the trace of all Module meta-classes and sub-classes declared
- **registry.neuron** is the dictionary keeping  the trace of all Neurons meta-classes and sub-classes declared

**⚠️** You can access and modify the registry manually. But it is advised to use it in a **readonly manner** if you want to avoid crashes due to lost classes.

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

### Neurons
Neuron is another meta-class designed to represent a neuron type. Each neuron is linked to its own synapse. (Read next section for more information about synapse). Neurons are also linked to a module by the `self.module`.
A neuron meta-class contains the three common field to the Module one with the same purposes:
- _name
- _register
- _abstract

Neuron, contrarily to Module, contains a constructor and several predefined method:

- \_\_init\_\_(self, module, threshold=0.3)
- add_output(self, output)
- remove_output(self, output)

To be traceable through the whole process each instanced neuron owns an id defined in `self.id` and following and incremental pattern starting at 1 (`Neuron.__next_id:int = 1`)

### Synapses

