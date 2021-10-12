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


class Random():
	def __init__(self, params):
		self.params      =  params
		self.memberships =  obj_clustering.getMemberships(self.params)

	def update(self, ed):
		ed.newaction						    	= np.random.choice(ed.actions, p=ed.randompolicy[ed.app])
		ed.newapp									= np.argmax(self.memberships[ed.newaction])

