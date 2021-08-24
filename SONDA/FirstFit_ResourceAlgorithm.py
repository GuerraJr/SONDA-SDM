import numpy as np

global n_slots
n_slots = 32

"""
The FirstFit class represents the First Fit spectrum assignment algorithm.
It tries to allocate the requisition on the first block of slots that are 
capable of containing the requisition.
"""

class FirstFit_ResourceAlgorithm:

    def __init__(self):  
        pass

    def FirstFit_ResourceAlgorithm(self, N, T, route, required_slots, core):
        aux = [1]*n_slots
        slots_list = [] 

        # checking which slots are available on all links of the route
        for r in range(len(route)-1): 
            rcurr = route[r]
            rnext = route[r+1]
            result = np.logical_and(aux, N[rcurr][rnext][core])
            aux = result

        # applying first-fit to the resulting list
        for s in range(n_slots-required_slots+1):
            for slot in range(s, s+required_slots, 1):
                if result[slot]: 
                    slots_list.append(slot)               
            if np.size(slots_list) == required_slots:            
                break           
            else:
                slots_list.clear()           

        return slots_list