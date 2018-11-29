import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import itertools


class Ising2D:

    equil_cycle = 1500 # determined graphically in Part 1

    def __init__(self, N, BJ, H=0.0):
        self.N = N # Grid dimension
        self.BJ = BJ # Beta (inverse temp) times J (spin coupling constant) 
        self.H = H # External magnetic field
        self.state = np.zeros((N,N)) # The 2D system of spins


    def run(self, initial_spin, steps=None, cycles=None, gif_name=None):
        
        # if user gave total steps convert to cycles
        if not cycles:
            cycles = steps // (self.N ** 2)

        print('\nRunning simulation for %d cycles with initial spins %s' % (cycles, initial_spin))

        # clear out data from previous runs 
        self.E = np.zeros(cycles+1) 
        self.M = np.zeros(cycles+1) 

        self.E_all = []
        self.M_all = []

        self.fig_viz = plt.figure() # For visualizing the model
        self.ax_viz = self.fig_viz.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
        self.images = [] # image snapshots of the model
        self.fig_graph, self.ax_graph = plt.subplots()

        # reset spins to specified distribution
        if initial_spin is 'up': 
            self.state.fill(1)
        elif initial_spin is 'down': 
            self.state.fill(-1)
        elif initial_spin is 'random':
            self.state = 2*np.random.rand(self.N,self.N)
            self.state = 2*self.state.astype(int)-1

        # calculate energy and magnetization of the initial spins 
        currM = np.sum(self.state)
        currE = -currM*self.H
        for i,j in itertools.product(range(self.N),range(self.N)):
            currE -= self.state[i,j] * ( self.state[(i+1) % self.N,j]
                                       + self.state[i,(j+1) % self.N] )

        # save a snapshot of the initial conditions
        self.snapshot("Cycle  0 \nBJ        %.4f\nH         %.4f" % (self.BJ, self.H))
        self.E[0] = currE
        self.M[0] = currM

        self.E_all.append(currE)
        self.M_all.append(currM)

        for cycle in range(1,cycles+1):

            # attempt N^2 moves per cycle 
            for step in range(self.N ** 2):
                i, j = np.random.randint(self.N, size=2)
                dE, dM = self.monte(i,j)
                currE += dE
                currM += dM
                self.E_all.append(currE)
                self.M_all.append(currM)
            self.E[cycle] = currE 
            self.M[cycle] = currM

            if cycle % 10 is 0 and gif_name:
                self.snapshot("Cycle  %d \nBJ        %.4f\nH         %.4f" % (cycle, self.BJ, self.H))

        # combine all of the snapshots into a gif
        if gif_name:
            self.gif(gif_name)
        self.ax_graph.plot(self.E)
        plt.close(self.fig_viz)

        self.fig_graph.savefig('testfile.png')
        plt.close(self.fig_graph)


    def monte(self,i,j):

        # change in magnetization and energy if spin[i,j] is flipped 
        dM = -2*self.state[i, j]
        dE = 2*self.state[i,j] * ( self.state[(i-1) % self.N, j] 
                                 + self.state[(i+1) % self.N, j]
                                 + self.state[i, (j-1) % self.N] 
                                 + self.state[i, (j+1) % self.N] )
        dE += -dM*self.H

        # condition for a monte_carlo move
        if dE < 0 or np.random.rand() < np.exp(-1*self.BJ*dE) :
            self.state[i,j] *= -1
            return dE, dM
        else:
            return 0, 0
        
    def stats(self):
        
        E_equil = np.array(self.E_all[(self.N ** 2) * self.equil_cycle + 1:])
        M_equil = np.array(self.M_all[(self.N ** 2) * self.equil_cycle + 1:])

        m_av = np.average(M_equil) / (self.N ** 2)
        e_av = np.average(E_equil) / (self.N ** 2)
        m2_av = np.average(np.multiply(M_equil,M_equil)) / (self.N ** 4)
        e2_av = np.average(np.multiply(E_equil,E_equil)) / (self.N ** 4)
        m_sigma = np.sqrt(m2_av -  m_av ** 2)
        e_sigma = np.sqrt(e2_av -  e_av ** 2)

        return m_av, e_av, m_sigma, e_sigma

    def snapshot(self, label):
        plt_image = self.ax_viz.imshow(self.state, cmap='seismic', interpolation='nearest', animated=True, vmin=-1, vmax=1)
        plt_text = self.ax_viz.text(0, 0, label, color='white', fontsize=16, transform=self.ax_viz.transAxes)
        self.ax_viz.axis('off')
        self.images.append([plt_image,plt_text])


    def gif(self,filename):
        print("Saving gif to \'%s\' of length %i frames" % (filename, len(self.images)))
        animation = anim.ArtistAnimation(self.fig_viz, self.images)
        animation.save(filename, writer='imagemagick', fps=10)

if __name__ == "__main__":
    pass
