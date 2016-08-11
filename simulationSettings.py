kb = 1.380e-23 # Boltzmann (J/K)
N_A = 6.022e23 # Molecules/mol

sigma = 3.4e-10 # [m] sigma in Lennard-Jones Potential
epsilon= kb*120 # [J] epsilon in Lennard-Jones Potential
cutOff = 2.25*sigma

mass = (39.95/N_A)*(10**-3) # [Kg] mass of a single atom; 39 --> Ar
boxSize = 10.229*sigma


