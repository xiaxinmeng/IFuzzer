# equivalent of perl's "while (<>) { ... } "
for line in ichain(all_lines_of(f) for f in list_of_filenames):
   do_something_with(line)

# generate infinite sequence 1,1,1,2,2,2...
seq = ichain(repeat(i,3) for i in count(1))