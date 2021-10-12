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


class ADR():
	def __init__(self, params):
		self.params  = params
		self.memberships =  obj_clustering.getMemberships(self.params)

	def update(self, ed):
		ed.newsf  = ed.sf
		ed.newptx = ed.ptx
		snr       = -300
		q1        = queue.Queue()
		while not ed.PP.empty():
			elm = ed.PP.get()
			snr = max(snr, elm.snr)
			q1.put(elm)
		ed.PP = q1
		ii  = snr - self.params.snrx[ed.drx] - 5
		ii /= 3
		ii  = int(ii)
		while ii != 0:
			if ii < 0:
				if ed.newptx < 10:
					ed.newptx +=3
				else:
					break
				ii+=1
			else:
				if ed.packets[ed.bestbs.id].dr > self.params.drx[ed.drx]:
					if ed.newptx > 13:
						ed.newptx -=3
					else:
						break
				elif ed.newsf > 7:
					ed.newsf-=1
				ii-=1
		for n, i in enumerate(ed.setActions):
				if i[0] == ed.freq and i[1] == ed.newsf and i[2] == ed.newptx and i[3] == ed.bw and i[4] == ed.cr:
					ed.newaction														= n
					ed.newapp																= np.argmax(self.memberships[ed.newaction])
					break

