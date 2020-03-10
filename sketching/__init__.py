from pygame.constants import *
from .tracer import Tracer
from .script import Script
from .constants import *
from .commands import *
from .util import *

def init(screen_size, fillcolor=(0,0,0)):
	pygame.init()
	DATA.screen=pygame.display.set_mode(screen_size)
	DATA.surface=pygame.Surface(screen_size)
	DATA.fillcolor=fillcolor
	DATA.surface.fill(DATA.fillcolor)

def quit():
	pygame.quit()

def clear():
	DATA.surface.fill(DATA.fillcolor)

def tracer(color=(255,255,255), linewidth=1, position=P2Vector(), angle=0, state=1):
	DATA.tracers.append(Tracer(color, linewidth, position, angle, state))
	return DATA.tracers[len(DATA.tracers)-1]

def update():
	DATA.screen.fill((0,0,0))
	for tracer in DATA.tracers:
		tracer.draw(DATA.surface)
	DATA.screen.blit(DATA.surface, (0,0))
	pygame.display.flip()

def running():
	return DATA.running

def stop():
	DATA.running=False

def events():
	return pygame.event.get()

def mouse():
	return pygame.mouse.get_pos()

def surface():
	return DATA.surface.copy()

def command(name, *args):
	return COMMANDS[name](*args)

def add_command(command):
	name=command().name
	COMMANDS[name]=command

def load_script(filename):
	commands=[]
	data=json.load(open(filename, 'r'))
	for i in range(len(data['commands'])):
		name=data['commands'][i]['name']
		args=data['commands'][i]['args']
		command=COMMANDS[name](*args)
		commands.append(command)
	return Script(commands)

def save_script(script, filename):
	commands=[]
	for i in range(len(script)):
		name=script[i].name
		args=script[i].args
		command={'name':name, 'args':args}
		commands.append(command)
	data={'commands': commands}
	json.dump(data, open(filename, 'w'))
	print('Saved script to '+filename+'.')