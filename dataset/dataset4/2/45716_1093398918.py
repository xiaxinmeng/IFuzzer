def start(x):
	x.start()
	
if __name__ == "__main__":
	import hotshot
	prof = hotshot.Profile("test3_stats")
	start(prof)
	#prof.start()	
	prof.stop()
	prof.close()
	from hotshot import stats
	s = stats.load("test3_stats")