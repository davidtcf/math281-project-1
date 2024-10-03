import numpy as np
import matplotlib.pyplot as plt


Nmodes = 10

def f(x):
    return np.sin(Nmodes * x)

def f_prime(x):
    return np.cos(Nmodes * x) * Nmodes

Lx = 2*np.pi
Nxs = np.power(2, np.arange(2, 9))

# Create some arrays to store the error values
err_2 = np.zeros(Nxs.shape)
err_4 = np.zeros(Nxs.shape)

# Create 
gridspec_props = dict(wspace = 0.05, hspace = 0.5, left = 0.1, right = 0.8, bottom = 0.1, top = 0.9)
fig, axes = plt.subplots(3, 1, figsize=(10,12), gridspec_kw = gridspec_props)

for Nx, ind in zip(Nxs, range(len(Nxs))):
    
    # Grid with chosen resolution
    x  = np.linspace(0, Lx, Nx)[:-1]
    Delta_x = x[1] - x[0]
    
    # Function to differentiation
    y  = f(x)
    
    # True derivative
    yp = f_prime(x)
    
    # Compute the numerical derivatives
    Ord2 = (                      np.roll(y, -1) -   np.roll(y, 1)                 ) / ( 2*Delta_x)
    Ord4 = ( - np.roll(y, -2) + 8*np.roll(y, -1) - 8*np.roll(y, 1) + np.roll(y, 2) ) / (12*Delta_x)
    
    # Store the error in the derivatives
    err_2[ind] = np.sqrt(np.mean( (Ord2 - yp)**2 ))
    err_4[ind] = np.sqrt(np.mean( (Ord4 - yp)**2 ))
    
    # Plot the derivative on the figure
    axes[1].plot(np.append(x, Lx), np.append(Ord2, Ord2[0]), '.-', label='Nx={0:d}'.format(Nx))
    axes[2].plot(np.append(x, Lx), np.append(Ord4, Ord4[0]), '.-', label='Nx={0:d}'.format(Nx))

    
##
## Add some formatting to the figures, and plot the error values.
##
axes[1].set_title('Order 2 Derivative')
axes[2].set_title('Order 4 Derivative')
for ax in axes[1:]:
    ax.set_xlabel('x')
    ax.set_ylabel('dydx')
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
    
axes[0].plot(Lx/Nxs, err_2, '-o', label='2nd order')
axes[0].plot(Lx/Nxs, err_4, '-o', label='4th order')
axes[0].plot(Lx/Nxs, (Lx/Nxs)**2, '--k', label='$dx^2$')
axes[0].plot(Lx/Nxs, (Lx/Nxs)**4, '-.k', label='$dx^4$')


axes[0].legend(bbox_to_anchor=(1., 0, 0.25, 1))
axes[0].set_xlabel('$\Delta x$')
axes[0].set_ylabel('Finite Difference Error')
axes[0].set_xscale('log')
axes[0].set_yscale('log')
axes[0].set_title('Demonstration of Convergence Order')

for ax in axes:
    ax.grid(True)
    
axes[1].legend(bbox_to_anchor=(1., -1, 0.25, 2))

plt.savefig('Question_2.pdf')
plt.show()
