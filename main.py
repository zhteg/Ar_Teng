# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:08:08 2016

@author: tzhan
"""
from atom.atomSubMain import Atoms
from integration.IntegrationSubMain import Simulation

numAtoms = 864 # Number of atoms to simulate
targetTemp=90 # K
eSteps,pStep=300， 500# Number of steps to equilibrate and produce data
# steps for NVT, do temp rescale every "nvtRelaxation" step or when temp deviates above "tempBound" 
nvtLength, nvtRelaxation, tempBound =200, 30, 10 

logFreq=5

"""initialization: add atom, create velocity, force update"""
atoms=Atoms(numAtoms) # adding atoms by sigma distance
atoms.applyGaussian(targetTemp) # assign initial velocity
atoms.momentumCorrection()
atoms.kineticEnergy()
print "Temperature=",atoms.temperature()
atoms.updateForces()

"""NVT equaliriate structures"""
for timestepID in range(0, nvtLength):
    atoms.nvt(atoms.velocityRescale,targetTemp,nvtRelaxation,tempBound)
    atoms.dump2log(5)
    atoms.dump2vmd(5)
    #print timestepID

"""NVE production run"""
for timestepID in range(0, eSteps):
    atoms.nve()
    atoms.dump2log(5)
    atoms.dump2vmd(5)
    
for timestepID in range(0, eSteps):
    atoms.nve()
    atoms.dump2log(5)
    atoms.dump2vmd(5)
    
