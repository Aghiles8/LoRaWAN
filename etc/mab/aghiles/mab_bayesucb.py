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


class bayesUCB():
	def __init__(self, params):
		self.params  		= params
		self.memberships =  obj_clustering.getMemberships(self.params)
		self.policy			= mybandit.bayesUCB (int(self.params.edDict[0].actions) , mybandit.Beta)

	def update(self, ed):
		self.policy.getReward(ed.action, ed.reward[ed.action][ed.app])
		ed.policy[ed.edapp]						= [self.policy.computeIndex(i) for i in range(ed.actions)] 
		ed.policy[ed.edapp]						= [0 if math.isinf(ed.policy[ed.edapp][i]) else ed.policy[ed.edapp][i] for i in range(ed.actions)]  
		ed.policy[ed.edapp]						= [ed.policy[ed.edapp][x]/sum(ed.policy[ed.edapp]) for x in range(0, ed.actions)]


#np.random.choice([arm for arm in ed.policy[ed.edapp].keys() if ed.policy[ed.edapp][arm] == max (ed.policy[ed.edapp].values())])
#np.random.choice([arm for arm in ed.policy[ed.edapp].keys() if ed.policy[ed.edapp][arm] == max (ed.policy[ed.edapp].values())])
