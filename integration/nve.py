from  simulationSettings import*

def nve():
    def verletIntegration(self):
        """Moves the system through a given time step, according to the energies"""
        global mass, dt,boxSize
        self.KE_flag=1
        for atom in self.atoms:

            # Update positions
            newX = atom.x + atom.vx*dt+0.5*(atom.fx/mass)*dt
            newY = atom.y + atom.vy*dt+0.5*(atom.fy/mass)*dt
            newZ = atom.z + atom.vz*dt+0.5*(atom.fz/mass)*dt

            # Update current positions (applying PBC)
            atom.x=newX-newX//boxSize
            atom.y=newX-newY//boxSize
            atom.z=newX-newZ//boxSize
        
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