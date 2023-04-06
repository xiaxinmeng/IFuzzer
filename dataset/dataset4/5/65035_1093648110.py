class Login():
    users = {}
    
    def __init__(self):
        try:
            with open('user.data','rb') as f:
                import pickle
                self.users = pickle.load(f)
#                print('init: {}'.format(self.users))
        except Exception:
            #'user.data' file doesn't exist
            pass

    def __del__(self):
        try:
            with open('user.data','wb') as f:
#                print('del: {}'.format(self.users))
#                print(type(self.users))
#                print(type(f))
                import pickle
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print('__del__ Shit happened: {}'.format(e))