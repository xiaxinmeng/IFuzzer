def test():
    print("In function test of pyemb.py file \n")    
    import pickle
    with open('filepath', 'rb') as f_in:
        C = pickle.load(f_in)