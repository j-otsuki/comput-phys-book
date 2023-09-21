import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def save_animation(x, t, u_tx, ymin, ymax, filename):
    fig = plt.figure()
    def plot(i):
        plt.cla()
        plt.title("t = %f" % t[i])
        plt.xlabel("$x$")
        plt.ylabel("$u(x)$")
        plt.ylim((ymin, ymax))
        plt.plot(x, u_tx[i, :])

    anim = animation.FuncAnimation(fig, plot, frames=u_tx.shape[0], interval=100, repeat=False)
    # plt.show()

    # Save animation
    anim.save(filename, writer="pillow")  # writer="pillow" or "imagemagick" for GIF
    print("saved as '{}'".format(filename))


def main():
    # Load results
    npz = np.load("kdv_solve_ivp.npz")
    print("npz.files =", npz.files)

    x = npz['x']
    t = npz['t']
    u_tx = npz['u_tx']
    print("x.shape =", x.shape)
    print("t.shape =", t.shape)
    print("u_tx.shape =", u_tx.shape)

    # make an animation
    print("Making animation...")
    save_animation(x, t, u_tx, ymin=-1.5, ymax=3.0, filename="kdv_solve_ivp.gif")


if __name__ == '__main__':
    main()
