urllib.parse.quote('http://127.0.0.1/[foo]bar.file?a=b&c=字')
'http%3A//127.0.0.1/%5Bfoo%5Dbar.file%3Fa%3Db%26c%3D%E5%AD%97' # invalid for some apps and browsers too