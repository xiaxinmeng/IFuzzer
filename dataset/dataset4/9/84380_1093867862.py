import warnings

compile("'\d'", "<string>", "eval")
warnings.resetwarnings()
compile("'\d'", "<string>", "eval")