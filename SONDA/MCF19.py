from MCF import MCF
from PhysicalConstants import K, beta, R, D
from UnitConversion import abs_to_db
#import numpy as np


class MCF19(MCF):

    def __init__(self, links, n_nodes, n_cores, n_slots, adjlist):
        super().__init__(links, n_nodes, n_cores, n_slots)
        self.adjlist = adjlist

    def worst_case(self, route, core, a):
        h = (2 * (K[2] ** 2) * R[2]) / (beta * D[2])
        if core == 0 or core == 2 or core == 4 or core == 6 or core == 8 or core == 10:
            nc = 3
        elif core == 1 or core == 3 or core == 5 or core == 7 or core == 9 or core == 11:
            nc = 4
        else:
            nc = 6
        xt = xt = 0.000000000000001
        for r in range(len(route) - 1):
            rcurr = route[r]
            rnext = route[r + 1]
            l_link = a[rcurr][rnext] * 1000
            xt += self.xt_calculator(h, l_link, nc)
        xt_db = abs_to_db(xt)
        return xt_db

