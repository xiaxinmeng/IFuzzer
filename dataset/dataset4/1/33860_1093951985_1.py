mm = re.compile("Processing (.+)?:\nFragments: (\d+)?");

output = os.popen("contig -a -s *.*");