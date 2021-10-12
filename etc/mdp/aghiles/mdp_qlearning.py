import csv
import sys
import random
import math
import copy
import queue
import numpy as np
#import etc.mab.general as mybandit
#import fcmeans
from   copy import deepcopy
#from   net.sim.tools import tools, logs
from etc.obj.aghiles import obj_clustering

class Qlearning():
	def __init__(self, params):
		self.params      = params
		self.memberships =  obj_clustering.getMemberships(self.params)

	def update(self, ed,):
		ed.policy[ed.app][ed.action]	= (1 - self.params.alpha) * ed.policy[ed.app, ed.action] + (self.params.alpha) * (ed.reward[ed.action][ed.app] + self.params.discount * np.max(ed.policy[ed.app]))
		ed.newaction					= random.randint(0, ed.actions-1) if np.random.uniform(0, 1) > self.params.alpha else np.argmax(ed.policy[ed.app]) # np.random.choice(ed.actions, p=ed.policy[ed.app])
		ed.newapp						= np.argmax(self.memberships[ed.newaction])

