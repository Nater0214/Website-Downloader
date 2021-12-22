import requests #imports

website = input("Website to download: ") #get the website data
data = requests.get(website)
data = data.text

name = input("Name of the file: ") #get the name of the file

file = open(name + ".html", "a") #create the file

for i in data: #I honestly have no idea what this does or how it works, I was trying to fix an issue and this fixed it.
    try:
        file.write(i)
    except:
        pass