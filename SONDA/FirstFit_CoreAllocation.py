import numpy as np
from FirstFit_ResourceAlgorithm import n_slots

class FirstFit_CoreAlloacation:
    def __init__(self):
        pass

    def FirstFit_CoreAlloacation(self, N, route, required_slots, n_cores):
        dimension = (n_cores, n_slots)
        FFmatrix = np.zeros(shape=dimension, dtype=np.uint8)
        slots_list = []
        core = None

        # checking which slots are available on all links of the route
        for c in range(n_cores):
            aux = [1]*n_slots
            for r in range(len(route)-1): 
                rcurr = route[r]
                rnext = route[r+1]
                result = np.logical_and(aux, N[rcurr][rnext][c])
                aux = result   
            FFmatrix[c] = result   

        # applying first-fit to the resulting matrix
        for c in range(n_cores):    
            for s in range(n_slots-required_slots+1):
                for slot in range(s, s+required_slots, 1):
                    if FFmatrix[c][slot]: 
                        slots_list.append(slot)
                if np.size(slots_list) == required_slots:
                    break               
                else:
                    slots_list.clear()
            if slots_list:            
                core = c
                break      
            
        return core