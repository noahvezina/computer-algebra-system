from operations import Operation

class Variable(Operation):
	def __init__(self, value: str):
		self.value = value
	
	def __repr__(self):
		return self.value
