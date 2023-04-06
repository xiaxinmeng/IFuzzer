def start_pickle_load_thread():

    for x in range(2):
        load_thread = threading.Thread(target=pickle_load_thread)
        load_thread.daemon = True
        threads.append(load_thread)

    for x in threads:
        x.start()


if __name__ == '__main__':

    start_pickle_load_thread()

    for t in threads:
        t.join()