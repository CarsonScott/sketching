class Script(list):
	def __init__(self, commands):
		super().__init__(commands)
		self.done=False
		self.index=0

	def execute(self, tracer):
		if not self.done:
			self[self.index].execute(tracer)
			self.index+=1
			if self.index >= len(self):
				self.done=True
		return self.done

	def reset(self):
		self.index=0
		self.done=False