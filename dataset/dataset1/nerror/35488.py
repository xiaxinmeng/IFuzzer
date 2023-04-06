from pathlib import Path

path1 = Path('/var/local/log/apache/httpd.log')

assert path1.match('/var/local/log/**/*.log'), "This one works"
assert path1.match('/var/**/*.log'), "This one fails"
assert path1.match('/var/local/**/*.log'), "This one fails too"
