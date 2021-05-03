from MCF import MCF
from PhysicalConstants import K, beta, R, D
from UnitConversion import abs_to_db
#import numpy as np


class MCF12(MCF):

    def __init__(self, links, n_nodes, n_cores, n_slots):
        super().__init__(links, n_nodes, n_cores, n_slots)

    def worst_case(self, route, core, a):
        h = (2 * (K[1] ** 2) * R[1]) / (beta * D[1])
        nc = 2
        xt = 0.000000000000001
        for r in range(len(route) - 1):
            rcurr = route[r]
            rnext = route[r + 1]
            l_link = a[rcurr][rnext]*1000
            xt += self.xt_calculator(h, l_link, nc)
        print(xt)
        xt_db = abs_to_db(xt)
        return xt_db
