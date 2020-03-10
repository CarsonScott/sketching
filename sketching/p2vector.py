class P2Vector(list):
	def __init__(self, *data):
		if len(data)==0:data=[0,0]
		elif len(data)==1 and (isinstance(data[0], list) or isinstance(data[0], tuple)):data=data[0]
		super().__init__(data)

	@property
	def x(self):return self[0]

	@property
	def y(self):return self[1]

	@x.setter
	def x(self, x):self[0]=x

	@y.setter
	def y(self, y):self[1]=y
	
	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self-type(self)([other for i in range(len(self))])
		else:
			output=type(self)()
			for i in range(len(self)):
				output[i]=self[i]-other[i]
			return output

	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self+type(self)([other for i in range(len(self))])
		else:
			output=type(self)()
			for i in range(len(self)):
				output[i]=self[i]+other[i]
			return output

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self*type(self)([other for i in range(len(self))])
		else:
			output=type(self)()
			for i in range(len(self)):
				output[i]=self[i]*other[i]
			return output

	def __truediv__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self/type(self)([other for i in range(len(self))])
		else:
			output=type(self)()
			for i in range(len(self)):
				output[i]=self[i]/other[i]
			return output

	def __lt__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self < type(self)([other for i in range(len(self))])
		else:
			for i in range(len(self)):
				if not self[i] < other[i]:
					return False
			return True

	def __gt__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self > type(self)([other for i in range(len(self))])
		else:
			for i in range(len(self)):
				if not self[i] > other[i]:
					return False
			return True 

	def __eq__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self == type(self)([other for i in range(len(self))])
		else:
			for i in range(len(self)):
				if not self[i] == other[i]:
					return False
			return True

	def __le__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self <= type(self)([other for i in range(len(self))])
		else:
			for i in range(len(self)):
				if not self[i] <= other[i]:
					return False
			return True 

	def __ge__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return self >= type(self)([other for i in range(len(self))])
		else:
			for i in range(len(self)):
				if not self[i] >= other[i]:
					return False
			return True 