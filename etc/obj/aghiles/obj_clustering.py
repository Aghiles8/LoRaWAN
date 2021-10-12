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

def getMemberships(params):
#		self.params.edDict[0].packets[0].dist	 	= 13000
#		self.params.edDict[0].packets[0].ps1	 	= 60
#		param															= {action:copy.copy(self.params.edDict[0].packets[0].update2(action)) for action in range(len(self.params.edDict[0].setActions))}
#		self.params.edDict[0].packets[0].id 		= -1
#		metrics 																= np.array([(pkt.ber, pkt.toa, pkt.dr) for pkt in param.values()], dtype=np.float32)
#		metricsx 																= np.zeros_like(metrics, dtype=np.int)
##		labels 																	= np.zeros_like(metrics)

#		for j in range(1):
#			s         = metrics[:,j]
#			sort_data = sorted(range(len(s)), key=lambda k: s[k])
#			for i in range(len(s)):
#				metricsx[sort_data[i],j] = 0 if i < (len(s)/1.8) else 1 if i < (len(s)/1.2) else 2

#		labels = [2 if metrics[i,0] < 0.385 else 1 if metrics[i,0] < 0.41 else 0 for i in range(len(metrics[:,0]))]
##		labels = metricsx[:,0]
#		print(labels)
#		out = np.zeros((len(labels),3))
#		for i in range(len(labels)):
#			out[i,labels[i]] = 1

#		np.savetxt(self.params.topopath+'fcm/0_fcm_i.csv', out , delimiter=',',  fmt='%d')
#		out = np.loadtxt(self.params.topopath+'fcm/0_fcm_i.csv', dtype='int'  , delimiter=',', skiprows=0)

##		np.savetxt(self.params.topopath+'fcm/0_fcm_u.csv', fcm.u , delimiter=',',  fmt='%1.3f')
#		np.savetxt(self.params.topopath+'fcm/0_fcm_x.csv', labels, delimiter=',',  fmt='%01d')
#		np.savetxt(self.params.topopath+'fcm/0_fcm_a.csv', self.params.edDict[0].setActions, delimiter=',', fmt='%04.1f,%01d,%02d,%03d,%01d')
#		np.savetxt(self.params.topopath+'fcm/0_fcm_m.csv', metrics, delimiter=',', fmt='%05.4f')
##		np.savetxt(self.params.topopath+'fcm/1_fcm_y.csv', metricsx, delimiter=',', fmt='%d')

#		u = np.loadtxt(self.params.topopath+'fcm/0_fcm_u.csv', dtype='float', delimiter=',', skiprows=0)
	l = np.loadtxt(params.topopath+'fcm/0_fcm_x.csv', dtype='int'  , delimiter=',', skiprows=0)
	s = np.loadtxt(params.topopath+'fcm/0_fcm_i.csv', dtype='int'  , delimiter=',', skiprows=0)

#		labels = [0 if metrics[i] < 0.2 else 1 if metrics[i] < 0.8 else 2 for i in range(len(metrics))]
#		fcm 																		= fcmeans.FCM(n_clusters=3,max_iter=1500,m=3,error=1e-5,random_state=443).fit(metricsx)
#		labels																	= [np.argmax(fcm.u[x]) for x in range(0, len(self.params.edDict[0].setActions))]

##		metricsx 																= np.array([(
##			2 if pkt.toa/1000 < 0.3   else 1 if  pkt.toa/1000 < 0.6   else 0, 
##			2 if pkt.ber      < 0.36  else 1 if  pkt.ber      < 0.41  else 0, 
##			2 if pkt.dr       < 2.3   else 1 if  pkt.dr       < 4.6     else 0) for pkt in param.values()], dtype=np.int)
#		print(metricsx)
##		out = np.zeros_like(fcm.u)
##		out[np.arange(len(fcm.u)), np.argpartition(fcm.u,-1, axis=1)[:,-1]] = 1
##		np.savetxt(self.params.topopath+'fcm/0_fcm_i.csv', out , delimiter=',',  fmt='%d')
	return s


