from bs4 import BeautifulSoup
import requests
import os
 
url_source = input("Please input website url:")
image_limit = int(input("Please input image download limit(0 for no limit):"))
img_file = input("Please input save format(jpg or png):")
 
response = requests.get(url_source)
soup = BeautifulSoup(response.text, "lxml")

if(image_limit == 0):
    results = soup.find_all("img")
else:
    results = soup.find_all("img", limit = image_limit)
 
image_links = [result.get("src") for result in results]  
 
for index, link in enumerate(image_links):
    
    # new a folder named "images" if there isn't one
    # all downloaded images will be saved in the folder
    if not os.path.exists("images"):
        os.mkdir("images")  
 
    # download images
    img = requests.get(link)  
 
    with open("images\\" + str(index+1) + "." + img_file, "wb") as file:  
        file.write(img.content)  