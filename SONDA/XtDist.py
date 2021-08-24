from PhysicalConstants import K, beta, R, D
from UnitConversion import *
import numpy as np


class XtDist:

    def __init__(self):
        pass

    def xtdist(self, l, n_cores):
        if n_cores == 7:
            Nc = 6
            h = (2 * pow(K[0], 2) * R[0]) / (beta * D[0])
            xt = (Nc - Nc * np.exp(-(Nc + 1) * 2 * h * l))/(1 + Nc * np.exp(-(Nc + 1) * 2 * h *l))
            xtdb = abs_to_db(xt)
        elif n_cores == 12:
            Nc = 2
            h = (2 * pow(K[1], 2) * R[1]) / (beta * D[1])
            xt = (1 - 1 * np.exp(-(1 + 1) * 2 * h * l)) / (1 + 1 * np.exp(-(1 + 1) * 2 * h * l))
            xtdb = abs_to_db(xt)
        else:
            Nc = 6
            h = (2 * pow(K[2], 2) * R[2]) / (beta * D[2])
            xt = (Nc - Nc * np.exp(-(Nc + 1) * 2 * h * l)) / (1 + Nc * np.exp(-(Nc + 1) * 2 * h * l))
            xtdb = abs_to_db(xt)

        return xtdb