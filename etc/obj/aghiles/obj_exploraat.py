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


class EXPLoRaAT():
	def __init__(self, params):
		self.params  = params
#		self.memberships =  getMemberships(self.params)

		sf_v  = np.array(sf_vec)
		sf_o  = [sf_v[i] for i in range(6)]
	#	SF_old.append(sf_o)
		w     = np.array([1.0, 1.83, 3.33, 6.67, 13.34, 24.04])
		q     = np.array([1.0 / 1.0, 1.0 / 1.83, 1.0 / 3.33, 1.0 / 6.67, 1.0 / 13.34, 1.0 / 24.04])
		P     = sf_v * w
		old_p = 0
		p     = 1
		vec   = ([0, 0, 0, 0, 0, 0])
		while old_p != p:
			p_idx = tools.local_peaks_indexes(P)
			p     = old_p
			old_p = p_idx
			start = 0
			for i in range(0, len(p_idx)):
				count = (sum(P[start:(p_idx[i])] * q[start:(p_idx[i])])) / (sum(q[start:(p_idx[i])]))
				for j in range(start, p_idx[i]):
					P[j] = count
				start = p_idx[i]
	#	EXP_P.append(P)
		k_AT = P * q
		for i in range(0, len(k_AT)):
			vec[i] = round(k_AT[i])
	#	EXP_K.append(vec)
#		return vec

	def update(self, ed):
		return

