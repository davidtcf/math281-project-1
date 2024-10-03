import numpy as np
import matplotlib.pyplot as plt


delta_x = 0.1

Lx10 = 10
x_Lx10 = np.arange( delta_x / 2 - Lx10 / 2, Lx10 / 2, delta_x )
u_Lx10 = np.exp( -x_Lx10**2 )

dudx_Lx10 = ( np.roll(u_Lx10, -1) - np.roll(u_Lx10, 1) ) / ( 2 * delta_x )

Lx6 = 6
x_Lx6 = np.arange( delta_x / 2 - Lx6 / 2, Lx6 / 2, delta_x )
u_Lx6 = np.exp( -x_Lx6**2 )

dudx_Lx6 = ( np.roll(u_Lx6, -1) - np.roll(u_Lx6, 1) ) / ( 2 * delta_x )

Lx4 = 4
x_Lx4 = np.arange( delta_x / 2 - Lx4 / 2, Lx4 / 2, delta_x )
u_Lx4 = np.exp( -x_Lx4**2 )

dudx_Lx4 = ( np.roll(u_Lx4, -1) - np.roll(u_Lx4, 1) ) / ( 2 * delta_x )

Lx2 = 2
x_Lx2 = np.arange( delta_x / 2 - Lx2 / 2, Lx2 / 2, delta_x )
u_Lx2 = np.exp( -x_Lx2**2 )

dudx_Lx2 = ( np.roll(u_Lx2, -1) - np.roll(u_Lx2, 1) ) / ( 2 * delta_x )

gridspec_props = dict(left = 0.15, right = 0.75, bottom = .15, top = 0.9)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12,8), sharex=False, sharey=False, gridspec_kw = gridspec_props,  constrained_layout=True)

ax1.plot(x_Lx10, dudx_Lx10, ':', label = 'Lx = 10')

ax1.legend(bbox_to_anchor=(1., 0, 0.35, 1))

ax1.set_xlim(-5, 5)

ax1.set_xlabel('x')
ax1.set_ylabel('du/dx')

ax2.plot(x_Lx6, dudx_Lx6, ':', label = 'Lx = 6')

ax2.legend(bbox_to_anchor=(1., 0, 0.35, 1))

ax2.set_xlim(-3, 3)

ax2.set_xlabel('x')
ax2.set_ylabel('du/dx')

ax3.plot(x_Lx4, dudx_Lx4, ':', label = 'Lx = 4')

ax3.legend(bbox_to_anchor=(1., 0, 0.35, 1))

ax3.set_xlim(-2, 2)

ax3.set_xlabel('x')
ax2.set_ylabel('du/dx')

ax4.plot(x_Lx2, dudx_Lx2, ':', label = 'Lx = 2')

ax4.legend(bbox_to_anchor=(1., 0, 0.35, 1))

ax4.set_xlim(-1, 1)

ax4.set_xlabel('x')
ax4.set_ylabel('du/dx')

plt.savefig('Question_1b.pdf')
plt.show()
