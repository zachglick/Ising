from ising import Ising2D

if __name__ == "__main__":

    # the 20x20 Ising Model 
    isingSmall = Ising2D(N=20, BJ=0.5)

    isingSmall.run(initial_spin='up', steps=1000000, gif_name='up1.gif')
    isingSmall.run(initial_spin='down', steps=1000000, gif_name='down1.gif')
    isingSmall.run(initial_spin='random', steps=1000000, gif_name='random1.gif')

    # the 60x60 Ising Model
    isingBig = Ising2D(N=60, BJ=0.5)

    isingBig.run(initial_spin='up', steps=1000000, gif_name='up2.gif')
    isingBig.run(initial_spin='down', steps=1000000, gif_name='down2.gif')
    isingBig.run(initial_spin='random', steps=1000000, gif_name='random2.gif')

    isingBig.run(initial_spin='up', steps=9000000, gif_name='up3.gif')
    isingBig.run(initial_spin='down', steps=9000000, gif_name='down3.gif')
    isingBig.run(initial_spin='random', steps=9000000, gif_name='random3.gif')

