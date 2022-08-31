import numpy as np

def get_v(state):
	return state[3:]

def free_particle(state):
	return 0,5*get_v(state)**2

state=np,array([1,2,3,4,5,6])
print(free_particle(state))