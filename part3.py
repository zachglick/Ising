import numpy as np
from ising import Ising2D
import matplotlib.pyplot as plt

if __name__ == "__main__":

    ising = Ising2D(N=20, BJ=0.5)

    # how much does this H change E (+-5% predicted)?
    for H in [-.00962, 0.0, 0.00962]:
        ising.H = H
        ising.run(initial_spin='up', steps=1000000, gif_name=None)
        m_av, e_av, m_sigma, e_sigma = ising.stats()
        print('  Magnetic field {:f}'.format(H))
        print('  e_av {:f}'.format(e_av))
        print('  m_av {:f}'.format(m_av))


    # scan temps, calc. e/m values
    e_ups = []
    e_downs = []
    m_ups = []
    m_downs = []
    H_range = np.linspace(-.1,.1,41)

    for H in H_range:
        ising.H = H
        ising.run(initial_spin='up', steps=1000000, gif_name=None)
        m_av, e_av, m_sigma, e_sigma = ising.stats()
        e_ups.append(e_av)
        m_ups.append(m_av)
        ising.run(initial_spin='down', steps=1000000, gif_name=None)
        m_av, e_av, m_sigma, e_sigma = ising.stats()
        e_downs.append(e_av)
        m_downs.append(m_av)


    fig, ax = plt.subplots()

    ax.plot(H_range, e_ups, label='Initial Up', linewidth=2, color='red', marker = '.')
    ax.plot(H_range, e_downs, label='Initial Down', linewidth=2, color ='blue', marker = '.')
    ax.set_xlabel(r'H')
    ax.set_ylabel(r'$\langle$ e $\rangle$')
    ax.legend(loc='upper left')
    plt.suptitle('External Field Dependence of Energy')
    plt.savefig('graphics/field_energy.png', dpi=300)

    fig2, ax2 = plt.subplots()

    ax2.plot(H_range, m_ups, label='Initial Up', linewidth=2, color='red', marker = '.')
    ax2.plot(H_range, m_downs, label='Initial Down', linewidth=2, color ='blue', marker = '.')
    ax2.set_xlabel(r'H')
    ax2.set_ylabel(r'$\langle$ m $\rangle$')
    ax2.legend(loc='upper left')
    plt.suptitle('External Field Dependence of Magnetization')
    plt.savefig('graphics/field_mag.png', dpi=300)


