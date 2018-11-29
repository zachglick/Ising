import numpy as np
import matplotlib.pyplot as plt
from ising import Ising2D

def onsager(BJ):
    """ analytic m(BJ)
    """
    if BJ < .44407:
        return 0
    else:
       return np.power(1-np.power(np.sinh(2*BJ),-4),.125)


if __name__ == "__main__":

    ising = Ising2D(N=20, BJ=0.5)

    # values of BJ around the critical point
    temp_range = np.arange(0.4,0.555,0.005)

    e_avs = []
    e_sigmas = []
    m_avs = []
    m_sigmas = []
    
    onsag = []

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
        onsag.append(onsager(temp))


    
    fig, ax = plt.subplots()
    ax.plot(temp_range, onsag, label='Analytic', linewidth=2, color='black')
    ax.plot(temp_range, m_avs, label='Monte Carlo', color ='blue', marker = '.')
    ax.fill_between(temp_range, np.array(m_avs), np.array(m_avs)-np.array(m_sigmas), color='blue', alpha = 0.5)
    ax.set_xlabel(r'$\beta$ J')
    ax.set_ylabel(r'$\langle$ m $\rangle$')
    ax.legend(loc='upper left')
    plt.suptitle('Temperature Dependence of Magnetization')
    plt.savefig('graphics/temp_mag.png')
    plt.show()
