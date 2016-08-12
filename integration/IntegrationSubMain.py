from  simulationSettings import*
import math

class Simulation(object):

    def nve(self):
        global mass, dt,boxSize
        self.KE_flag=1
        for atom in self.atoms:
            # Update positions
            newX = atom.x + atom.vx*dt+0.5*(atom.fx/mass)*dt**2
            newY = atom.y + atom.vy*dt+0.5*(atom.fy/mass)*dt**2
            newZ = atom.z + atom.vz*dt+0.5*(atom.fz/mass)*dt**2

            # Update positions (applying PBC)
            atom.x=newX-(newX//boxSize)*boxSize
            atom.y=newY-(newY//boxSize)*boxSize
            atom.z=newZ-(newZ//boxSize)*boxSize

            # Update velocities
            atom.vx += 0.5*(atom.fx/mass)*dt
            atom.vy += 0.5*(atom.fy/mass)*dt
            atom.vz += 0.5*(atom.fz/mass)*dt
        
        self.updateForces()
        
        for atom in self.atoms:
        
            # Update velocities
            atom.vx += 0.5*(atom.fx/mass)*dt
            atom.vy += 0.5*(atom.fy/mass)*dt
            atom.vz += 0.5*(atom.fz/mass)*dt  


    def velocityRescale(self,Temp):
        """rescale the velocities to the target temperature"""
        self.momentumCorrection()
        scalingFactor=math.sqrt(Temp/self.temperature())
        for atom in self.atoms:
            atom.vx*=scalingFactor
            atom.vy*=scalingFactor
            atom.vz*=scalingFactor

    def nvt(self,tempMethod,temp,relaxation,tempBound,timestepID):
        """tempMethod: velocityRescale; relaxation: timestep interval to perform Temperature"""
        self.nve()
        if timestepID % relaxation==0 or math.fabs(self.temperature()-temp) > tempBound:
            tempMethod(temp)
        
        
        

        
	