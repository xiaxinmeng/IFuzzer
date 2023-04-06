import io
import pickle
from datetime import datetime


def main():
    """
    Uses python 2.7 to create a pickle file with a datetime object inside a dictionary.
    """
    data = {}
    data['timenode'] = datetime.now()
    with io.open('written_by_py27.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()