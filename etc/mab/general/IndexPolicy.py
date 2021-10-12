#!/usr/bin/env python
from random import choice
from a7.bandit.policy.Policy import *

class IndexPolicy(Policy):

    def choice(self):
        """In an index policy, choose at random an arm with maximal index."""
        index = dict()
        for arm in range(self.nbArms):
            index[arm] = self.computeIndex(arm)
        maxIndex = max (index.values())
        bestArms = [arm for arm in index.keys() if index[arm] == maxIndex]
        return choice(bestArms)



