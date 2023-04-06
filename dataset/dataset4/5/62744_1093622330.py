cmd='gpg --passphrase-fd {fd} -c'.format(fd=fd)
with open('passphrase.txt','r') as fd3_fh:
    with open('filename.txt','r') as stdin_fh:
        with open('filename.gpg','w') as stdout_fh:        
            proc=subprocess.Popen(shlex.split(cmd),
                                  stdin=stdin_fh,
                                  stdout=stdout_fh,
                                  fd3=fd3_fh)
            proc.communicate()