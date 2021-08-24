import numpy as np


class MCF:
    def __init__(self, links, n_nodes, n_cores, n_slots):
        self.links = links
        self.n_nodes = n_nodes
        self.n_cores = n_cores
        self.n_slots = n_slots

    def genemcf(self):
        # init slots availability matrix
        dimension = (self.n_nodes, self.n_nodes, self.n_cores, self.n_slots)
        sslot = np.zeros(shape=dimension, dtype=np.uint8)
        for link in self.links:
            for core in range(self.n_cores):
                for s in range(self.n_slots):
                    slot_availability = 1
                    sslot[link[0]][link[1]][core][s] = slot_availability
                    sslot[link[1]][link[0]][core][s] = slot_availability

        # init traffic matrix
        dimension = (self.n_nodes, self.n_nodes, self.n_cores, self.n_slots)
        ttime = np.zeros(shape=dimension, dtype=np.float64)
        for link in self.links:
            for core in range(self.n_cores):
                for s in range(self.n_slots):
                    ttime[link[0]][link[1]][core][s] = 0
                    ttime[link[1]][link[0]][core][s] = 0

        return sslot, ttime

    def xt_calculator(self, h, ll, nc):
        xt = nc*(1 - np.exp(-(nc + 1) * 2 * h * ll)) / (1 + nc * np.exp(-(nc + 1) * 2 * h * ll))
        return xt

    def worst_case(self, route, core, a):
        # Return a value below the threshold values, if n_cores are not 7, 12 or 19
        return -100

