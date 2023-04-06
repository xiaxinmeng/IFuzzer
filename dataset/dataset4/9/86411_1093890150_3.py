def fit_model():
    # JUST CREATING A DATASET, NOT EVEN FITTING ANY MODEL!!! AND IT FREEZES
    data = make_regression(n_samples=500, n_features=100, n_informative=10, n_targets=1, random_state=5)
    # model = XGBRegressor(n_jobs = -1)
    # model.fit(data[0],data[1])
    print('Fit complete')

with concurrent.futures.ProcessPoolExecutor() as executor:
    results_temp = [executor.submit(fit_model) for i in range(0,12)]
# 