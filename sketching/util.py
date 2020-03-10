from .p2vector import P2Vector
import pygame
import json
import math

def degrees(a):
	return a*180/math.pi

def radians(a):
	return a*math.pi/180

def sign(x):
	return -1 if x < 0 else 1 if x > 0 else 0

def compute_angle(p1,p2):
	dx,dy=P2Vector(p2)-P2Vector(p1)
	return math.atan2(dy,dx)

def opposite_angle(a):
	return -sign(a)*math.pi+a

def translate_angle(a):
	if a >= math.pi:a = -math.pi + a % math.pi 
	elif a < -math.pi:a = math.pi - abs(a) % math.pi
	return a

def compute_position(origin, distance, angle):
	x=origin[0]+math.cos(angle)*distance
	y=origin[1]+math.sin(angle)*distance
	position=P2Vector(x,y)
	return position