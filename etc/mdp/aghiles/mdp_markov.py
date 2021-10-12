import csv
import sys
import random
import math
import copy
import queue
import numpy as np
import etc.mab.general as mybandit
#import fcmeans
from   copy import deepcopy
#from   net.sim.tools import tools, logs
from etc.obj.aghiles import obj_clustering

class Markov():
	def __init__(self, params):
		self.params      = params
		self.memberships = obj_clustering.getMemberships(self.params)

	def update(self, ed):
		values						= np.zeros(3)
		while True:	
			oldValues				= np.copy(values)
			values[ed.app]		= ed.reward[ed.action][ed.app] + np.max(self.params.discount * np.dot(self.memberships[:][:], values))
			if np.max(np.abs(values - oldValues)) <= 0.0001:
				break
		policies							= np.zeros([3, ed.actions])
		policies[ed.app]			= [ed.reward[j][ed.app] for j in range(ed.actions)] + self.params.discount * np.dot(self.memberships[:][:], values)
		policies[ed.app]			= np.exp((policies[ed.app] - np.max(policies[ed.app])) / float(self.params.tau))
		ed.policy[ed.app]			= policies[ed.app] / policies[ed.app].sum() 
		ed.newaction					= np.random.choice(ed.actions, p=ed.policy[ed.app])
		ed.newapp							= np.argmax(self.memberships[ed.newaction])

#  = np.random.choice(policies[ed.app], p=ed.policy[ed.app]) #np.random.choice(np.array(np.where(policies[ed.app][:] == policy)).ravel())



#	def update(self, ed):
#		V				= np.zeros(3)
#		R				= ed.reward[ed.action][ed.app]
#		while True:	
#			V1		= np.copy(V)
#			V[s]	= R + np.max(self.params.discount * np.dot(self.memberships[:][:], values))
#			if np.max(np.abs(V - V1)) <= 0.0001:
#				break
#		P											= {s:max(ed.actions, key=lambda a: sum([p * V[s1] for (p, s1) in T[s][a]])) for s in range(3)}
#		ed.newaction					= np.random.choice(ed.actions, p=P)
#		ed.newapp							= np.argmax(self.memberships[ed.newaction])




