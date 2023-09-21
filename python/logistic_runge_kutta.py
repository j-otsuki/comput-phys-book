import numpy as np
import matplotlib.pyplot as plt


# define df/dt
def f_logistic(y):
    return y * (1.0 - y)


# Runge-Kutta method of order 4
def step_forward(f, y, dt):
    k1 = f(y)
    k2 = f(y + k1 * dt / 2)
    k3 = f(y + k2 * dt / 2)
    k4 = f(y + k3 * dt)
    return y + (k1 + 2*k2 + 2*k3 + k4) * dt / 6


# Solve ODE
def solve_ode(f, y0, tmax, nt):
    t = np.linspace(0, tmax, nt)
    dt = t[1] - t[0]
    y = [y0,]
    for _ in range(nt-1):
        y.append(step_forward(f, y[-1], dt))
    return t, np.array(y)


def main():
    t, y = solve_ode(f_logistic, y0=1e-3, tmax=20, nt=101)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(t, y, '.')
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    fig.savefig("logistic.pdf")


if __name__ == '__main__':
    main()
