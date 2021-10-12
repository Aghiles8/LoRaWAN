import csv
import sys
import random
import math
import copy
import queue
import numpy as np
import etc.mab.general as mybandit
from   copy import deepcopy
from etc.obj.aghiles import obj_clustering


class ContextThompson():
	def __init__(self, params):
        nchoices                = y.shape[1]
        # base_algorithm          = LogisticRegression(solver='lbfgs', warm_start=True)
        # beta_prior              = ((3./nchoices, 4), 2) 					# until there are at least 2 observations of each class, will use this prior
        # beta_prior_ucb          = ((5./nchoices, 4), 2) 					# UCB gives higher numbers, thus the higher positive prior
        beta_prior_ts           = ((2./np.log2(nchoices), 4), 2)  # Important!!! the default values for beta_prior will be changed in version 0.3
        # bootstrapped_ucb        = BootstrappedUCB(deepcopy(base_algorithm)    , nchoices = nchoices,beta_prior = beta_prior_ucb, percentile = 80,random_state = 1111) ## The base algorithm is embedded in different metaheuristics
        # bootstrapped_ts         = BootstrappedTS(deepcopy(base_algorithm)     , nchoices = nchoices,beta_prior = beta_prior_ts, random_state = 2222)
        # one_vs_rest             = SeparateClassifiers(deepcopy(base_algorithm), nchoices = nchoices,beta_prior = beta_prior, random_state = 3333)
        # epsilon_greedy          = EpsilonGreedy(deepcopy(base_algorithm)      , nchoices = nchoices,beta_prior = beta_prior, random_state = 4444)
        logistic_ucb            = LogisticUCB(                                  nchoices = nchoices,percentile = 70,beta_prior = beta_prior_ts, random_state = 5555)
        # adaptive_greedy_thr     = AdaptiveGreedy(deepcopy(base_algorithm)     , nchoices = nchoices,decay_type='threshold',beta_prior = beta_prior, random_state = 6666)
        # adaptive_greedy_perc    = AdaptiveGreedy(deepcopy(base_algorithm)     , nchoices = nchoices,decay_type='percentile', decay=0.9997,beta_prior=beta_prior, random_state = 7777)
        # explore_first           = ExploreFirst(deepcopy(base_algorithm)       , nchoices = nchoices,explore_rounds=1500, beta_prior=None, random_state = 8888)
        # active_explorer         = ActiveExplorer(deepcopy(base_algorithm)     , nchoices = nchoices,beta_prior=beta_prior, random_state = 9999)
        # adaptive_active_greedy  = AdaptiveGreedy(deepcopy(base_algorithm)     , nchoices = nchoices,active_choice='weighted', decay_type='percentile', decay=0.9997,beta_prior=beta_prior, random_state = 1234)
        # softmax_explorer        = SoftmaxExplorer(deepcopy(base_algorithm)    , nchoices = nchoices,beta_prior=beta_prior, random_state = 5678)
        # models                  = [bootstrapped_ucb, bootstrapped_ts, one_vs_rest, epsilon_greedy, logistic_ucb,adaptive_greedy_thr, adaptive_greedy_perc, explore_first, active_explorer,adaptive_active_greedy, softmax_explorer]
        model                   = logistic_ucb

        self.params  		                	= params
		self.memberships                        = obj_clustering.getMemberships(self.params)
		self.policy			                	= mybandit.Thompson (int(self.params.edDict[0].actions), mybandit.Beta)

	def update(self, ed):
		self.policy.getReward(ed.action, ed.reward[ed.action][ed.app])
		ed.policy[ed.edapp]						= [self.policy.computeIndex(i) for i in range(ed.actions)] 
		ed.policy[ed.edapp]						= [0 if math.isinf(ed.policy[ed.edapp][i]) else ed.policy[ed.edapp][i] for i in range(ed.actions)]  
		ed.policy[ed.edapp]						= [ed.policy[ed.edapp][x]/sum(ed.policy[ed.edapp]) for x in range(0, ed.actions)]


#np.random.choice([arm for arm in ed.policy[ed.edapp].keys() if ed.policy[ed.edapp][arm] == max (ed.policy[ed.edapp].values())])
#np.random.choice([arm for arm in ed.policy[ed.edapp].keys() if ed.policy[ed.edapp][arm] == max (ed.policy[ed.edapp].values())])
