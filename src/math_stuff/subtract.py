from operations import Operation

class Subtraction(Operation):
	def __init__(self, value1: Operation, value2: Operation):
		self.value1 = value1
		self.value2 = value2
	
	def __repr__(self):
		return f"{self.value1} - {self.value2}"
