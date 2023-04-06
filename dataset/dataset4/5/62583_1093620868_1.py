simplefilter("error")
simplefilter("ignore", append=True)  # appends new filter to the end

simplefilter("ignore")
simplefilter("error", append=True)
simplefilter("ignore", append=True)  # does nothing since same filter is present.