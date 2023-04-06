from urllib.request import urlopen
 
data = urlopen("https://cinnamon-spices.linuxmint.com/json/applets.json").read()
 
print(data)