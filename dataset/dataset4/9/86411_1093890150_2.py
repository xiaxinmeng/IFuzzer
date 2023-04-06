def just_print():
    print('Just printing')

with concurrent.futures.ProcessPoolExecutor() as executor:
    results_temp = [executor.submit(just_print) for i in range(0,12)]
# 