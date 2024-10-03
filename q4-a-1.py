import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 10})


final_time = 5.

Nx = 400

CFL = np.array([0.01,0.1,0.5])


for i in range(len(CFL)):

    delta_x = 10 / Nx
    delta_t = CFL[i] * delta_x


    x = np.arange(delta_x / 2. - 5, 5, delta_x)

    Nt = Nt = int( np.ceil(final_time / delta_t) ) + 2
    t = np.zeros(Nt)
    t[0] = 0.

    solution = np.zeros((Nt,Nx))
    solution[0,:] = np.exp( - ((x-2.5)/(0.5))**2 )

    curr_time = t[0]
    u = solution[0,:]

    output_number = 0
    while curr_time < final_time:
        
        # Compute the RHS of the ODE (2*t)
        dudt = ( np.roll(u, -1) - np.roll(u, 1) ) / ( 2 * delta_x )
        
        # Update first-order record
        u = u + delta_t * dudt
        
        # Increase 'time' by Delta t
        curr_time = curr_time + delta_t
        
        # Store the new values in our array
        output_number = output_number + 1
        solution[output_number,:] = u
        t[output_number] = curr_time
        
    # Helps to avoid odd errors from funky step sizes
    t = t[:output_number]
    solution = solution[:output_number,:]

    gridspec_props = dict(left = 0.1, right = 0.9, bottom = 0.1, top = 0.85)

    fig, axes = plt.subplots(1, 1, sharex=True, figsize = (7, 5), gridspec_kw = gridspec_props)

    plt.pcolormesh(x, t, solution, cmap = 'gray', rasterized = True) # the 'rasterized' piece is only necessary for saving to pdfs

    plt.colorbar()
    plt.grid(color='r', linestyle='--')

    plt.xlabel('x')
    plt.ylabel('t')

    plt.title('Advection Solution\nCFL = {0:g}, Delta x = {1:g}'.format(CFL[i], delta_x))
    plt.show()
