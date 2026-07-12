from operations import Operation

class Constant(Operation):
	def __init__(self, value):
		self.value = value
	
	def __repr__(self):
		return str(self.value)
	
	
if __name__ == "__main__":
	const1 = Constant(4)
	print(const1)
