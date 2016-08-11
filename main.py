# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:08:08 2016

@author: tzhan
"""
from atom.atomSubMain import Atoms
from integration.IntegrationSubMain import simulation

numAtoms = 864 # Number of atoms to simulate
nSteps=10 # Number of steps to simulate
targetTemp=50 # K

atoms=Atoms(numAtoms) # adding atoms by sigma distance
atoms.applyGaussian(targetTemp)
atoms.momentumCorrection()
atoms.kineticEnergy()
print "Temperature=",atoms.temperature()

atoms.updateForces()
i=366
print atoms.atoms[i].fx,atoms.atoms[i].fy,atoms.atoms[i].fz
for step in range(0, nSteps):
    # Run the simulation for a single step
    simulation()