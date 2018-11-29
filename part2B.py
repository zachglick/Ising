import numpy as np
import matplotlib.pyplot as plt
from ising import Ising2D

if __name__ == "__main__":

    ising = Ising2D(N=20, BJ=0.5)

    temp_range = np.linspace(0.5, 0.55, 6)
    cv_anas = []
    cv_nums = []

    for BJ in temp_range:

        print('Determining Heat Capacity for BJ of {:f}'.format(BJ))
        ising.BJ = BJ
        ising.run(initial_spin='up', cycles = 2500, gif_name=None)
        m_av, e_av, m_sigma, e_sigma = ising.stats()
        
        # analytic heat capacity
        cv_ana = BJ * (e_sigma ** 2) * (ising.N ** 2)

        # numerical heat capacity taken by finite differences
        isingPlus = Ising2D(N=20, BJ=BJ+0.01)
        isingPlus.run(initial_spin='up', cycles = 2500, gif_name=None)
        m_avP, e_avP, m_sigmaP, e_sigmaP = isingPlus.stats()

        isingMinus = Ising2D(N=20, BJ=BJ-0.01)
        isingMinus.run(initial_spin='up', cycles = 2500, gif_name=None)
        m_avM, e_avM, m_sigmaM, e_sigmaM = isingMinus.stats()

        dEdBJ = (e_avP - e_avM)/0.02 
        cv_num = - (BJ ** 2) * dEdBJ
        print("Calculated dE/dBJ: {:f}".format(dEdBJ))
        print("Cv analytical: {:f}".format(cv_ana))
        print("Cv numerical: {:f}".format(cv_num))
        cv_anas.append(cv_ana)
        cv_nums.append(cv_num)
        
    fig, ax = plt.subplots()

    ax.plot(temp_range, cv_anas, label='Analytic', linewidth=2, color='black', marker = '.')
    ax.plot(temp_range, cv_nums, label='Finite Differences', color ='blue', marker = '.')
    ax.set_xlabel(r'$\beta$ J')
    ax.set_ylabel(r'$C_v$')
    ax.set_ylim(bottom=0.0)
    ax.legend(loc='lower left')
    plt.suptitle('Temperature Dependence of Heat Capacity')
    plt.savefig('graphics/temp_cv.png', dpi=300)

