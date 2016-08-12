# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:08:08 2016

@author: tzhan
"""
from atom.atomSubMain import Atoms
from integration.IntegrationSubMain import Simulation
from numpy import inf

numAtoms = 864 # Number of atoms to simulate
targetTemp=90 # K
eNvtSteps, eNveSteps,pNveSteps=200, 200, 450# Number of steps to equilibrate and produce data
# steps for NVT, do temp rescale every "nvtRelaxation" step or when temp deviates above "tempBound" 
nvtRelaxation, tempBound = 30, 10 
logFreq,xyzFreq=5, 5 # Output Frequency for log.txt and vmd.xyz

binNum,binWidth,binFreq=250,0.02,5 #Rdf
autoVstart=nvtLength+eSteps #velocity Autocorrelation starts at autoVstart timestep

"""initialization: add atom, create velocity, force update"""
atoms=Atoms(numAtoms) # adding atoms by sigma distance
atoms.applyGaussian(targetTemp) # assign initial velocity


"""NVT equilibrate structures"""
for timestepID in range(0, eNvtSteps):
    atoms.nvt(atoms.velocityRescale,targetTemp,nvtRelaxation,tempBound,logFreq,xyzFreq)
   
    
"""NVE furthuer quilibrium"""
for timestepID in range(0, eNveSteps):
    atoms.nve(logFreq,xyzFreq)

"""NVE production run"""    
for timestepID in range(0, pNveSteps):
    atoms.pairDistributionFunction(binNum,binWidth,binFreq)
    atoms.velocityAutocorrelation(autoVstart)    
    atoms.nve(logFreq,xyzFreq)

