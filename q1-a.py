import numpy as np
import matplotlib.pyplot as plt


delta_x = 0.1

# Note that this grid could also be created using various built-in functions, such as:
#  grid_1 = np.linspace(0, 0.9, 10)
#  grid_1 = np.arange(0, 1, 0.1)
grid_1 = np.array([0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
grid_2 = np.array([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95])
grid_3 = np.array([0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
U_grid1 = np.sin( 2 * np.pi * grid_1 )
U_grid2 = np.sin( 2 * np.pi * grid_2 )
U_grid3 = np.sin( 2 * np.pi * grid_3 )

dudx_grid1 = ( np.roll(U_grid1, -1) - np.roll(U_grid1, 1) ) / ( 2 * delta_x )
dudx_grid2 = ( np.roll(U_grid2, -1) - np.roll(U_grid2, 1) ) / ( 2 * delta_x )
dudx_grid3 = ( np.roll(U_grid3, -1) - np.roll(U_grid3, 1) ) / ( 2 * delta_x )


gridspec_props = dict(left = 0.1, right = 0.75, bottom = 0.15, top = 0.9) # you can adjust these numbers to adjust the margins in your figures
fig, axes = plt.subplots(1, 1, figsize=(7,4), gridspec_kw = gridspec_props)

plt.plot(grid_1, dudx_grid1, '-o', label = 'Grid 1')
plt.plot(grid_2, dudx_grid2, '-o', label = 'Grid 2')
plt.plot(grid_3, dudx_grid3, '-o', label = 'Grid 3')

plt.legend(bbox_to_anchor=(1., 0, 0.3, 1))

plt.xlim(0, 1)

plt.xlabel('x')
plt.ylabel('du/dx')

plt.savefig('Question_1a.pdf')
plt.show()
