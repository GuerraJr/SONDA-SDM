"""
    c: light's velocity.
    h: Planck's constant.
    l: light's wavelength.
    freq: light's frequency.
    BRef:  reference bandwidth.
    numPolarizations: is used to choose whether one or two polarizations are used to transmit the signal.
    k: coupling coefficient.
    beta: propagation constant.
    R: bend radius.
    D: core pitch.

"""
 
c = 299792458
h = 6.62606957E-34
l = 1550E-9
freq = 193.4E12
BRef = 12.5E9
BSlot = 12.5E9    
numPolarizations = 2


K = [2E-5, 7.34E-5, 3.5E-4]
beta = 4E6
R = [50E-3, 140E-3, 80E-3]
D = [45E-6, 37E-6, 35E-6]