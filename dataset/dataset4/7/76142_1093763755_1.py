# runs this weird file
subprocess.run([bin])

# Currently an error; if this is implemented, would run
# /bin/ls, and pass it the -l argument. Refers to something
# completely different than our .exists() call above.
subprocess.run(bin)