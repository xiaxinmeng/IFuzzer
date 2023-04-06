settings_file = open('settings.txt','r')
settings = [line.strip() for line in settings_file.readlines()]
# Filter out comments and empties
settings = [line for line in settings if (line!='' and line[0] != '#')]