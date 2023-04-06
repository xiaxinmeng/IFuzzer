import concurrent.futures
from sklearn.datasets import make_regression

def just_print():
    print('Just printing')

def fit_model():
    data = make_regression(n_samples=500, n_features=100, n_informative=10, n_targets=1, random_state=5)
    print('Fit complete')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_temp = [executor.submit(just_print) for i in range(0,12)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_temp = [executor.submit(fit_model) for i in range(0,12)]