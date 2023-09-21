import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xlim = (-40, 40)
ylim = (0, 0.4)
basename = "schr"

npz = np.load(basename + ".npz")
x, t, v = npz['x'], npz['t'], npz['v']
u_tx = npz['u_tx']
rho = np.absolute(u_tx)**2

# common setting for plot
fig, ax = plt.subplots(figsize=(6, 3), constrained_layout=True)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$|\psi(x)|^2$")
ax.set_xlim(xlim)
ax.set_ylim(ylim)

print("Making animation...")
artists = []
for i in range(t.size):
    # Make i-th plot
    artist = ax.plot(x, rho[i, :], '-b', lw=1, zorder=4)  # 確率密度
    artist += [ax.fill_between(x, rho[i, :], color="lightblue", alpha=0.5, zorder=3)]  # 塗りつぶし
    artist += ax.plot(x, v, color='k', lw=1, zorder=2)  # ポテンシャル
    artist += [ax.fill_between(x, v, color="lightgray", alpha=0.5, zorder=1)]  # 塗りつぶし
    artist += [ax.text(0.05, 1.05, f"t = {t[i]:.2f}", transform=ax.transAxes)]
    artists.append(artist)

anim = animation.ArtistAnimation(fig, artists, interval=100, repeat=False)

file_gif = basename + '.gif'
anim.save(file_gif, writer="imagemagick")
print(f"'{file_gif}' generated")
