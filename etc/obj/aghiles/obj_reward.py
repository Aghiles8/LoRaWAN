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
#from etc.obj import obj_clustering


def objective(ed):
	reward = ((ed.dr_mean)) #*  ((ed.ber_mean) -1)
#	print (pkt.dr, reward)
	return reward
