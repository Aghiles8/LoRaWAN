#!/usr/bin/env python

import numpy as np

def main():
  N     = 3
  means = np.array([0.3, 0.7, 0.5])  # prob of a win, each machine
  probs = np.zeros(N)                # sampling prob win, each machine
  S     = np.zeros(N, dtype=np.int)  # number successes each machine
  F     = np.zeros(N, dtype=np.int)  # number failures each machine
  rnd   = np.random.RandomState(7)   # for machine payouts and Beta

  for trial in range(10):
    probs       = [rnd.beta(S[i] + 1, F[i] + 1) for i in range(N)]
    machine     = np.argmax(probs)
    p           = rnd.random_sample()
    S[machine] += 1 if p < means[machine] else  S[machine]
    F[machine] += 1 if p >= means[machine] else F[machine]

  print(S)
  print(F)

if __name__ == "__main__":
  main()



import random

N                    = 10000
d                    = 10
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d

    if reward == 1:
        numbers_of_rewards_1[ad] += 1
    else:
        numbers_of_rewards_0[ad] += 1

    ad         = 0
    max_random = 0

    for i in range(ed.actions):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i













