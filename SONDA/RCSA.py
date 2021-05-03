from PhysicalConstants import BSlot
from Dijkstra_RoutingAlgorithm import Dijkstra
from FirstFit_ResourceAlgorithm import *
from FirstFit_CoreAllocation import FirstFit_CoreAlloacation
from Signal import Signal 
from Modulation import Modulation
from MCF import MCF
from MCF7 import MCF7
from MCF12 import MCF12
from MCF19 import MCF19
import math

dijkstra = Dijkstra()
FF_resource = FirstFit_ResourceAlgorithm()
FF_core = FirstFit_CoreAlloacation()
signal = Signal()
modulation = Modulation()


class RCSA:

    def __init__(self):  
        pass
   
    def Generate(self, n_nodes, n_cores, links):             

        if n_cores == 7:
            mcf = MCF7(links, n_nodes, n_cores, n_slots)
        elif n_cores == 12:
            mcf = MCF12(links, n_nodes, n_cores, n_slots)
        elif n_cores == 19:
            adjlist = []
            mcf = MCF19(links, n_nodes, n_cores, n_slots, adjlist)
        else:
            mcf = MCF(links, n_nodes, n_cores, n_slots)
        return mcf

    def RCSA(self, A, N, T, src_node, dst_node, holding_time, bit_rate, network_type, wavelength_bandwidth, consider_ase_noise, damp, number, n_cores, mcf, consider_xt):
        # defining the best route according to the dijkstra algorithm 
        route = dijkstra.Dijkstra(A, src_node, dst_node)

        M = modulation.M
        if number > 0 and number <= 25:
            SNRb = modulation.SNRb01
        elif number > 25 and number <= 50:   
            SNRb = modulation.SNRb02
        elif number > 50 and number <= 75:    
            SNRb = modulation.SNRb03
        else:    
            SNRb = modulation.SNRb04

        if network_type == 1:
            if consider_ase_noise == 0:
                required_slots = math.ceil((wavelength_bandwidth*10**9)/BSlot)
                xt_threshold = modulation.XtThreshold[2]
            else:
                bit_rate = (wavelength_bandwidth*10**9) * numPolarizations * math.log2(M[2])
                if signal.OutputOSNR(A, route, damp) > modulation.ThresholdOSNR(bit_rate, SNRb[2]): 
                    required_slots = math.ceil((wavelength_bandwidth*10**9)/BSlot) 
                    color = 0
                else:
                    return 1    
                xt_threshold = modulation.XtThreshold[2]
        else:            
            if consider_ase_noise == 0:
                required_slots = modulation.RequiredSlots(bit_rate, BSlot, M[2])
                xt_threshold = modulation.XtThreshold[2]
            else:                
                for i in range(3):
                    if signal.OutputOSNR(A, route, damp) > modulation.ThresholdOSNR(bit_rate, SNRb[i]):
                        required_slots = modulation.RequiredSlots(bit_rate, BSlot, M[i])
                        xt_threshold = modulation.XtThreshold[i]
                        color = 0
                        break
                    else:
                        color = 1      
                if color:        
                    return 1             
            
        # defining first core available 
        core = FF_core.FirstFit_CoreAlloacation(N, route, required_slots, n_cores)
        if core == None:   
            return 1

        # defining the slots to be allocated 
        slots_vector = FF_resource.FirstFit_ResourceAlgorithm(N, T, route, required_slots, core)


        # Crosstalk consideration
        if slots_vector:
            if consider_xt == 0:
                pass
            else:
                #Slots are going to be allocated if the xt level is less than threshold value
                if mcf.worst_case(route, core, A) <= xt_threshold:
                    pass
                else:
                    return 1
            # if all specifications are answered, allocate resources on the links of the route
            for r in range(len(route)-1):
                rcurr = route[r]
                rnext = route[r+1]
                for i in range(required_slots):
                    N[rcurr][rnext][core][slots_vector[i]] = 0
                    T[rcurr][rnext][core][slots_vector[i]] = holding_time
            return 0  # allocated
        else:
            return 1  # blocked
