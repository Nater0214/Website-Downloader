import requests #imports

website = input("Website to download: ") #get the website data
data = requests.get(website)
data = data.text

name = input("Name of the file: ") #get the name of the file

file = open(name + ".html", "a")

for i in data:
    try:
        file.write(i)
    except:
        pass