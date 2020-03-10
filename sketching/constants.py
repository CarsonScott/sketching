from .data import Data
from .commands import *
from .util import *

RIGHT=0
LEFT=math.pi
UP=-math.pi*0.5
DOWN=math.pi*0.5

COMMANDS={
	'Rotate': Rotate,
	'Color': Color,
	'Angle': Angle,
	'Move': Move,
	'Off': Off,
	'On': On,
}

DATA=Data()