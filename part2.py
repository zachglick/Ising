import numpy as np
import matplotlib.pyplot as plt
from ising import Ising2D

def onsager(BJ):
    """ analytic m(BJ)
    """
    if BJ < 4.4401:
        return 0
    else:
       return np.pow(1-np.pow(np.sinh(2*BJ),-4),-.125)


if __name__ == "__main__":

    ising = Ising2D(N=20, BJ=0.5)

    # values of BJ around the critical point
    temp_range = np.arange(0.4,0.555,0.005)

    e_avs = []
    e_sigmas = []
    m_avs = []
    m_sigmas = []

    for temp in temp_range:

        ising.BJ = temp
        ising.run(initial_spin='up', cycles = 2500, gif_name=None)
        m_av, e_av, m_sigma, e_sigma = ising.stats()

        print('e_av    {:f}'.format(e_av))
        print('e_sigma {:f}'.format(e_sigma))
        print('m_av    {:f}'.format(m_av))
        print('m_sigma {:f}'.format(m_sigma))

        e_avs.append(e_av) 
        e_sigmas.append(e_sigma) 
        m_avs.append(m_av) 
        m_sigmas.append(m_sigma) 



    fig, ax = plt.subplots()
    ax.plot(number_python.arange(0.4,0.56,0.01), flucts, label='mag. sigma')
    plt.show()
