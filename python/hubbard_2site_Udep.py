import numpy as np
import matplotlib.pyplot as plt

from hubbard_2site import solve_hubbard_2site

def main():
    t = 1.0
    n = 2
    # n = None

    U_min = 0
    U_max = 10
    N = 201

    U_list = []
    ene_list = []
    for U in np.linspace(U_min, U_max, N):
        # mu = 0.5 * U
        mu = 0
        ene, _ = solve_hubbard_2site(t, U, mu=mu, n=n)
        U_list.append(U)
        ene_list.append(ene)

    # save as a text file
    U_np = np.array(U_list)  # shape=(N,)
    ene_np = np.array(ene_list)  # shape=(N, 6)
    np.savetxt("energy.dat", np.hstack([U_np[:, None], ene_np]))

    # plot
    fig, ax = plt.subplots()
    ax.plot(U_np, ene_np)
    ax.set_xlabel("$U / t$")
    ax.set_ylabel("$E / t$")
    fig.savefig("hubbard_2site_Udep.pdf")
    # plt.show()

if __name__ == '__main__':
    main()
