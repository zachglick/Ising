# Ising

## Part 1: Determining Monte Carlo Parameters
  
   A 2-dimensional spin Ising model of size 20x20 was constructed. The temperature/spin coupling parameter, BJ, was set to 0.5 (below the critical temperature) and 1,000,000 Monte Carlo moves were performed, where each move constituted an attempt to flip a randomly selected spin from the crystal. This simulation was performed with three different initial spin distributions: all up, all down, and randomly oriented:
   
  [3 side by side gifs. Each gif shows spins(t), E(t), M(t)]
  Repeated this test multiple times to see if the behavior was predictable:
  [time series with multiple trajectories]
  This does/doesn't agree with Onsager's result
  
  b) Reran the same test for a 60x60 Ising model. Used the same number of steps (10^6). 
  [3 side by side gifs. Each gif shows spins(t), E(t), M(t)] 
  Does the final system depend on the choice of initial conditions in a different way than before?  
  If yes, is this a problem, and what could be causing this problem?
  
  c) Reran the 60x60 test for the same number of cycles as the 20x20 test. A cycle is N^2 steps, so this was 10^6 * (60)^2 / (20)^2 = 9 * 10^6 steps
  Noted things about equilibrium time that did/didn't made these two tests equivalent
  
## Part 2: Exploring Critical Behavior
  
  a) Computed <E>, <E^2>, <M>, <M^2> after equilibration period:
  b) Temperature dependence of magnetization
  c) Numerical evaluation of sigma_E and sigma_M
  d) Heat capacity (numerical temperature derivative)
  
## Part 3: External Magnetic Field

  a) Implement this additional Hamiltonian term in your MC code
  b) You can estimate the relative strength of the field by how much the energy of the
system changes relative to the zero field case.For βJ=0.5, what is the average magnetization
without the field?  What is the average energy?  Assuming that the magnetization doesn’t
change (e.g.  zero susceptibility), calculate the applied field H (in units of J/μ) required to
change the energy by 5%.  Apply this external field, and calculate the resulting magnetiza-
tion and energy in the presence of the field.  Comment on your results
  c) The external field breaks the symmetry of the energy function w.r.t.  all spins up or
all spins down.  Thus, degeneracy is broken, and this is one unique energy minima.  However
there will still be a barrier for converting between states with all spins up and all spins down.
Run different simulations starting from all spins up and all spins down in the presence of
the  external  field.   What  is  the  average  energy  of  these  different  simulations?   Do  these
simulations differ from the case of no field?  Comment on your observations as you increase
the strength of the external field.
