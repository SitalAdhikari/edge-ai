import numpy as np

class Neuron:
	def __init__(self,weights,bias):
		self.weights = weights
		self.bias = bias
	
	def weightage_sum(self,inputs):
		return  (np.dot(self.weights, inputs) + self.bias)
	
	def relu(self, inputs):
		z = self.weightage_sum(inputs)
		return np.maximum(0,z)
		
	
neuron= Neuron([0.1,0.2,0.3],0.5)
print(neuron.weightage_sum([1,1,-3]))
print(neuron.relu([1,1,-3]))
