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
from   app import app



class EXPLoRaTS():
	def __init__(self, params):
		self.params  = params
#		self.memberships =  getMemberships(self.params)

		edDict        = self.params.edDict
		T             = float(1)
		w             = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
		q             = np.array([1.0 / 1.0, 1.0 / 2.0, 1.0 / 4.0, 1.0 / 8.0, 1.0 / 16.0, 1.0 / 32.0])
		N_sym_sf      = np.array([0, 0, 0, 0, 0, 0])
		sf_o          = ([0, 0, 0, 0, 0, 0])
		bucket_nodes  = ([0, 0, 0, 0, 0, 0])
		sf_n          = ([0, 0, 0, 0, 0, 0])
		no_edDict     = []
		old_p         = 0
		p             = 1
		bsid          = 0

		for nd in range(0, len(edDict)):
			if edDict[nd].minBS == bsid:
				MP                      = float(edDict[nd].period)
				PL                      = float(edDict[nd].ps1)
				SF                      = float(edDict[nd].sf)
				N_mess                  = T / MP

				N_sym_mess              = 8 + max(math.ceil((2.0 * PL - SF + 11) / SF) * 5, 0)
				N_sym_usr               = N_sym_mess * N_mess
				N_sym_sf[int(SF - 7)]   = N_sym_sf[int(SF - 7)] + N_sym_usr
				sf_o[int(SF - 7)]       = sf_o[int(SF - 7)] + 1
				edDict[nd].symboltime = N_sym_usr

		P            = N_sym_sf * w
		k_TS         = P * q

		while old_p != p:
			p_idx = app.local_peaks_indexes(P)
			p     = old_p
			old_p = p_idx
			start = 0
			for i in range(0, len(p_idx)):
				count = (sum(P[start:(p_idx[i])] * q[start:(p_idx[i])])) / (sum(q[start:(p_idx[i])]))
				for j in range(start, p_idx[i]):
					P[j] = count
				start = p_idx[i]

		for i in range(0, len(edDict)):
			bucket_nodes[edDict[i].sf - 7] += 1 if edDict[i].minBS == bsid else bucket_nodes[edDict[i].sf - 7]

		for bucket_sf in range(0, len(bucket_nodes)):
			pbucket = k_TS
			for ts_times in range(0, int(bucket_nodes[bucket_sf])):
				max_pl    = 0
				max_pl_id = 0
				for nd in range(len(edDict)):
					max_pl                 = edDict[nd].ps1    if edDict[nd].minBS == bsid and edDict[nd].sf == (bucket_sf + 7) and edDict[nd].ts == 0 and edDict[nd].ps1 > max_pl else max_pl
					max_pl_id              = nd                if edDict[nd].minBS == bsid and edDict[nd].sf == (bucket_sf + 7) and edDict[nd].ts == 0 and edDict[nd].ps1 > max_pl else max_pl_id
				if edDict[max_pl_id].symboltime <= pbucket[bucket_sf]:
					pbucket[bucket_sf]     = pbucket[bucket_sf] - edDict[max_pl_id].symboltime 
					edDict[max_pl_id].ts   = 1
				else:
					edDict[max_pl_id].sf          += 1
					if bucket_sf < 5:
						bucket_nodes[bucket_sf + 1] += 1
					MP                             = float(edDict[max_pl_id].period)
					PL                             = float(edDict[max_pl_id].ps1)
					SF                             = float(edDict[max_pl_id].sf)
					N_mess                         = T / MP
					N_sym_mess                     = 8 + max(math.ceil((2.0 * PL - SF + 11) / SF) * 5, 0)
					N_sym_usr                      = N_sym_mess * N_mess
					edDict[max_pl_id].symboltime = N_sym_usr

		for i in range(0, len(edDict)):
			tmp = no_edDict.append(i) if edDict[i].ts == 0 and edDict[i].minBS == bsid else 0

		for ts_times in range(0, len(no_edDict)):
			edDict[int(no_edDict[ts_times])].sf         = edDict[int(no_edDict[ts_times])].initial_sf
			MP                                          = float(edDict[int(no_edDict[ts_times])].period)
			PL                                          = float(edDict[int(no_edDict[ts_times])].ps1)
			SF                                          = float(edDict[int(no_edDict[ts_times])].sf)
			N_mess                                      = T / MP
			N_sym_mess                                  = 8 + max(math.ceil((2.0 * PL - SF + 11) / SF) * 5, 0)
			N_sym_usr                                   = N_sym_mess * N_mess
			edDict[int(no_edDict[ts_times])].symboltime = N_sym_usr

			for bucket_sf in range(int(edDict[int(no_edDict[ts_times])].sf - 7), 6):
				max_bucket_sf                          = int(edDict[int(no_edDict[ts_times])].sf - 7)
				max_bucket                             = pbucket[max_bucket_sf]
				max_bucket                             = pbucket[bucket_sf] if pbucket[bucket_sf] > max_bucket else max_bucket
				max_bucket_sf                          = bucket_sf          if pbucket[bucket_sf] > max_bucket else max_bucket_sf

			pbucket[max_bucket_sf]                   = pbucket[max_bucket_sf] - edDict[int(no_edDict[ts_times])].symboltime
			edDict[int(no_edDict[ts_times])].ts  = 1

		for test in range(0, len(edDict)):
			sf_n[edDict[test].sf - 7] += 1 if edDict[test].minBS == bsid else sf_n[edDict[test].sf - 7]

		for nd in range(0, len(edDict)):
			edDict[nd].ts = 0 if edDict[nd].ts == 1 and edDict[nd].minBS == bsid else edDict[nd].ts
#		return edDict

	def update(self, ed):
		return



