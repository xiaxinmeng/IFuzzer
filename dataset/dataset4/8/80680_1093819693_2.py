import io
import pickle


def main():
    """
    Attempts to unpickle a dictionary with a datatype object inside
    """
    with io.open('written_by_py27.pickle', 'rb') as handle:
        unpickler = pickle._Unpickler(handle)
        unpickler.encoding = 'latin1'
        pkl = unpickler.load()
        print("Pickle: ", pkl)

if __name__ == "__main__":
    main()