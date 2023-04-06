path_explorers = threading.ThreadGroup('path_explorers')
for path in paths:
    threading.Thread(path_explorers, explore, (path,))
for thread in path_explorers: # enumerate unfinished explorers
    print(thread)
path_explorers.start()        # begin parallel search
path_explorers.join()         # wait for group to finish
print("Result:", best_path)