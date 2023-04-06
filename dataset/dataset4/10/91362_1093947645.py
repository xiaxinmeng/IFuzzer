import pickle


class X:
    class Y:
        pass

    def method(self):
        pass


print(pickle.dumps(X.Y))
print(pickle.loads(pickle.dumps(X.Y)))

print(pickle.dumps(X.Y()))
print(pickle.loads(pickle.dumps(X.Y())))

print(pickle.dumps(X.method))
print(pickle.loads(pickle.dumps(X.method)))