from .util import *

class Tracer:
	def __init__(self, color, linewidth, position, angle, state):
		self.color=color
		self.linewidth=linewidth
		self.position=P2Vector(position)
		self.previous=P2Vector(position)
		self.angle=translate_angle(angle)
		self.state=state

	def set_position(self, xy):
		self.position=P2Vector(xy)

	def set_angle(self, a):
		self.angle=translate_angle(a)

	def set_color(self, rgb):
		self.color=rgb

	def set_linewidth(self, w):
		self.linewidth=w

	def set_state(self, s):
		self.state=s

	def off(self):
		self.state=0

	def on(self):
		self.state=1

	def move(self, r):
		position=compute_position(self.position, r, self.angle)
		self.set_position(position)

	def rotate(self, da):
		angle=self.angle+da
		self.set_angle(angle)

	def draw(self, surface):
		if self.position!=self.previous and self.state==1:
			pygame.draw.line(surface, self.color, self.previous, self.position, self.linewidth)
		self.previous=self.position