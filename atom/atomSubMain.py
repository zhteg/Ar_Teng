from atom import ArAtom as Atom
from integration.IntegrationSubMain import Simulation
import random 
from  simulationSettings import*

import math

class Atoms(Atom,Simulation):
    atoms = []
    numAtoms=0
    KE, KE_flag=0.0, 1
    PE=0
    def __init__(self,numAtoms):
        """initialize atom list by numAtoms"""
        self.numAtoms=numAtoms
        for i in range(0,self.numAtoms):
            self.atoms.append(Atom())
        self.assignPositions() # assign atom positions
        print "total %i atoms placed by %2.3f angstroms" % (self.numAtoms, sigma*10**10)
		
    def passAtom(self):
        """return atom list"""
        return self.atoms
		
    def assignPositions(self):
        """Place atoms by sigma (simulation setting) in the box."""
        global sigma

        n = int(math.ceil(self.numAtoms**(1.0/3))) # atomNum in one direction
        i = 0 # Particles placed so far
        for x in range(0, n):
            for y in range(0, n):
                for z in range(0, n):
                    if (i < self.numAtoms):
                        self.atoms[i].x = x * sigma
                        self.atoms[i].y = y * sigma             
                        self.atoms[i].z = z * sigma
                        i += 1
                    else:
                        return 0
                        
    def applyGaussian(self,Temp):
        """Applies guassian distribution to atomic velocities
        # the standard deviation of guassian distributin is approximately 
        related to temperature as sigma^2=kb*t/m
        http://www.ss.ncu.edu.tw/~lyu/lecture_files/2012Fall/Lyu_TD_Notes/2011_0927a_MaxwellianDistribution.pdf"""
        global kb,mass
        normDist = []
        stdGaussian = math.sqrt(kb*Temp/mass)
        
        # Establish Normal Distribution
        for i in range(0, 3*self.numAtoms):
            normDist.append(random.gauss(0,stdGaussian))
            
        # Distribute velocities
        for atom in range(0, self.numAtoms):
            self.atoms[atom].vx = normDist[atom*3]
            self.atoms[atom].vy = normDist[atom*3+1]
            self.atoms[atom].vz = normDist[atom*3+2]      
    
    def momentumCorrection(self):
        """ momentum --> 0"""
        self.KE_flag=1
        vSum, vAve=[0.0]*3, [0.0]*3
        for atom in self.atoms:
            vSum[0] += atom.vx
            vSum[1] += atom.vy
            vSum[2] += atom.vz
        for i in range(3):
            vAve[i]=vSum[i]/self.numAtoms
        for atom in self.atoms:
            atom.vx = atom.vx -vAve[0]
            atom.vy = atom.vy -vAve[1]
            atom.vz = atom.vz -vAve[2]   
            
    def kineticEnergy(self):
        """update KE if KE_flag !=0 (needs updated)"""
        if self.KE_flag:
            self.KE, self.KE_flag=0.0, 0
            for atom in self.atoms:
                self.KE+=(atom.vx**2+atom.vy**2+atom.vz**2)
            self.KE*=mass/2
        return self.KE
        
    def temperature(self):
        """update KE, return Temperature"""
        if self.KE_flag:
            self.kineticEnergy()
        return self.KE/self.numAtoms/1.5/kb
        
    def calculateForce(self, atom1, atom2):
        """Calculates the force between two atoms using LJ 12-6 potential"""
        global sigma, epsilon,cutOff, boxSize
   
        # Calculate distance between two atoms
        dx = self.atoms[atom1].x - self.atoms[atom2].x
        dy = self.atoms[atom1].y - self.atoms[atom2].y
        dz = self.atoms[atom1].z - self.atoms[atom2].z
        #print dx,dy,dz
        # Minimum Image Convention
        dx -= boxSize*round(dx/boxSize)
        dy -= boxSize*round(dy/boxSize)
        dz -= boxSize*round(dz/boxSize)
        #print "New",dx,dy,dz

        r2 = dx*dx + dy*dy + dz*dz

        if r2 < cutOff:
            fr2 = (sigma**2)/r2
            fr6 = fr2**3
            force = 48*epsilon*fr6*(fr6 - 0.5)/r2
            pot = 4*epsilon*fr6*(fr6 - 1)
            
            # Update forces
            self.atoms[atom1].fx += force*dx
            self.atoms[atom2].fx -= force*dx
            self.atoms[atom1].fy += force*dy
            self.atoms[atom2].fy -= force*dy
            self.atoms[atom1].fz += force*dz
            self.atoms[atom2].fz -= force*dz
            
            # Update potentials
            self.atoms[atom1].potential += pot/2.0
            self.atoms[atom2].potential += pot/2.0
            
    def updateForces(self):
        """Calculates the net potential on each atom, applying a cutoff radius"""
        self.resetForces()
        for atom1 in range(0, self.numAtoms-1):
            for atom2 in range(atom1+1, self.numAtoms):
                self.calculateForce(atom1, atom2)
                
    def resetForces(self):
        """Sets all forces to zero"""
        for atom in self.atoms:
            atom.fx = 0
            atom.fy = 0
            atom.fz = 0
            atom.potential = 0

    def potentialEnergy(self):
        """update KE if KE_flag !=0 (needs updated)"""
        self.PE=0
        for atom in self.atoms:
            self.PE+=atom.potential
        return self.PE