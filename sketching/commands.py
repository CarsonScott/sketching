class Command:
	def __init__(self, name, *args):
		self.name=name
		self.args=list(args)

	def __repr__(self):
		string=str(self.name)+'('
		for i in range(len(self.args)):
			string+=str(self.args[i])
			if i < len(self.args)-1:
				string+=', '
		string+=')'
		return string
	
	def execute(self, tracer):
		pass


class Move(Command):
	def __init__(self, *args):
		super().__init__('Move', *args)

	def execute(self, tracer):
		tracer.move(*self.args)


class Rotate(Command):
	def __init__(self, *args):
		super().__init__('Rotate', *args)

	def execute(self, tracer):
		tracer.rotate(*self.args)


class On(Command):
	def __init__(self, *args):
		super().__init__('On', *args)

	def execute(self, tracer):
		tracer.on(*self.args)


class Off(Command):
	def __init__(self, *args):
		super().__init__('Off', *args)

	def execute(self, tracer):
		tracer.off(*self.args)


class Color(Command):
	def __init__(self, *args):
		super().__init__('Color', *args)
	
	def execute(self, tracer):
		tracer.set_color(*self.args)


class Angle(Command):
	def __init__(self, *args):
		super().__init__('Angle', *args)

	def execute(self, tracer):
		tracer.set_angle(*self.args)
