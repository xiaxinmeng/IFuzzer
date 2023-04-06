while 1:
    vi.rate(20)
    # Draw state
    #Display(WF*conjugate(WF)).real*scale)
    Display(identity(resolution[0]))
    # Time step
    TimeStep()
    t+=step