from  simulationSettings import*
from tempRescale import tempRescale

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

            

        

        
	