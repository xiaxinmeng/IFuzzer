def profile_helper(pr):
    sys.setprofile(pr.dispatcher)
    # Function will return None, dead here

pr = profile.Profile()  # Create simulate_call
# We go into profile_helper, but didn't simulate a call!! (didn't setprofile yet)
profile_helper(pr)      
sys.setprofile(None)