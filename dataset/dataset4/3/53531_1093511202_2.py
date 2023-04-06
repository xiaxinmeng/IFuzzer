def profile_helper(pr):
    pr._adjust_frame()  # call simuate_call here
    sys.setprofile(pr.dispatcher)

pr = profile.Profile()  # Create simulate_call
profile_helper(pr)      
sys.setprofile(None)