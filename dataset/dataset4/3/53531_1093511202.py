pr = profile.Profile()  # It will call simulate_call at the end of init
sys.setprofile(pr.dispatcher)
# profile
sys.setprofile(None)