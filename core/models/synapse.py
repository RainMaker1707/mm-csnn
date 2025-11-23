from typing import List


class Synapse():
    def __init__(self, neuron):
        self.parent = neuron
        self.neurons: List['Neuron']= []

    def add(self, neuron):
        if neuron in self.neurons:
            raise ValueError(f'Multiple synaptic connection to the same neuron is not allowed. Neuron: {neuron.id} already connected to synapse')
        
        if neuron == self.parent:
            raise ValueError("Recursive synaptic connection not allowed!")
        
        self.neurons.append(neuron)

    def remove(self, neuron):
        if not neuron in self.neurons:
            raise ValueError(f'Neuron id: {neuron.id} cannot be removed because it is not connected to the synapse')
        self.neurons.remove(neuron)

    def spike(self, delay):
        for neuron in self.neurons:
            neuron.spike_in(self.parent, delay)
