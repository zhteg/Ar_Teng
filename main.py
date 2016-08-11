# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:08:08 2016

@author: tzhan
"""
from atom.atomSubMain import Atoms
from integration.IntegrationSubMain import Simulation

numAtoms = 864 # Number of atoms to simulate
nSteps=100 # Number of steps to simulate
targetTemp=90 # K

atoms=Atoms(numAtoms) # adding atoms by sigma distance
atoms.applyGaussian(targetTemp)
atoms.momentumCorrection()
atoms.kineticEnergy()
print "Temperature=",atoms.temperature()
atoms.updateForces()


for step in range(0, nSteps):
    atoms.nve()
    print "Temperature=",atoms.temperature()
