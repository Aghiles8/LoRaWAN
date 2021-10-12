#!/usr/bin/env python
from etc.mab.general.kullback import klucbGauss
from etc.mab.general.klUCB import klUCB

class UCB(klUCB):
    def __init__(self, nbArms, amplitude=1., lower=0.):
        klUCB.__init__(self, nbArms, amplitude, lower, lambda x, d, sig2: klucbGauss(x, d, .25))


