def traced(flag):
    if flag:
        return 1
    else:
        return 2

tracer = Trace()
tracer.runfunc(traced, False)
results = tracer.results()
results.write_results(coverdir='.')