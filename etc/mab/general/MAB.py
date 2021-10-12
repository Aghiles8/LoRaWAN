#!/usr/bin/env python
class MAB():

    def __init__(self, arms):
        self.arms = arms
        self.nbArms = len(arms)
        # supposed to have a property nbArms

     def play(self, policy, horizon):
        policy.startGame()
#        result = Result(self.nbArms, horizon)
        for t in range(horizon):
            choice = policy.choice()
            reward = self.arms[choice]
            policy.getReward(choice, reward)
#            result.store(t, choice, reward)
        return choice






