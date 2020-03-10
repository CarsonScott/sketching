# A Library for Working with Turtle Graphics in Pygame

_Sketching_ is a library for working with turtle graphics in pygame. It provides an interface for creating graphics using "scripts", or sets of instructions that automate the generation of different patterns, from basic 2D shapes to complex fractal images.

___

## Tracers
A tracer is an object that draws lines onto a pygame surface. Tracers move along the surface in order to generate lines, and are defined by a position and angle at any given point in time. Commands sent to a tracer prompt movement/rotation relative to its current position/angle and cause new lines to be drawn to the surface.

## Scripts
A Command is a basic building block that allows complex actions to be carried out through the use of a script. Scripts are sequences of commands that automate the generation of complex graphical patterns which are fed to a tracer sequentially over time.
