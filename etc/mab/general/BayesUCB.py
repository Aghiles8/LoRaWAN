#!/usr/bin/env python
from random import choice
from etc.mab.general import Beta as Posterior
from etc.mab.general.Policy import Policy

class BayesUCB(Policy):

    def __init__(self, nbArms, posterior):
        self.nbArms = nbArms
        self.posterior = dict()
        for arm in range(self.nbArms):
            self.posterior[arm] = posterior()

#    def startGame(self):
        self.t = 1;
        for arm in range(self.nbArms):
            self.posterior[arm].reset()

    def getReward(self, arm, reward):
        self.posterior[arm].update(reward)
        self.t += 1

    def computeIndex(self, arm):
        return self.posterior[arm].quantile(1-1./self.t)


