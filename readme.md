# Image Downloader

突發奇想來寫個爬蟲，原本是想用node.js寫的，但實在是太困難了，我不確定node做不做得到我想做的事，但反正我是做不到，果然爬蟲還是要用python。

做法是參考[這個網址](https://www.learncodewithmike.com/2020/09/download-images-using-python.html)，不過做了一些改動。

這次的目標是要讓使用者輸入網址之後，可以把該網址的image下載下來。
不過這個其實難度很高，應該說難的地方在於，沒辦法預測使用者想要什麼圖片，如果可以提前知道的話就可以用一些keywords去過濾，但反正只是一時興起做做，就弄了一個不過濾的downloader。


```
from bs4 import BeautifulSoup
import requests
import os
```

一樣是使用BS4跟requests，額外import了一個os，用來方便使用者如果沒有創建資料夾的話可以自動建立一個。

------

```
url_source = input("Please input website url:")
image_limit = int(input("Please input image download limit(0 for no limit):"))
img_file = input("Please input save format(jpg or png):")
```

前面先用三個input，分別讓使用者輸入網址、下載圖片上限數、以及想要存的格式。
原版是直接把url寫在code裡，但畢竟沒辦法預先知道使用者想從哪個網站下載圖片，所以要讓使用者輸入。
而要限制上限的原因是，因為是無腦的把整個網頁有img tag的東西都抓下來，如果是像什麼購物網站之類，有超級爆炸多圖片的網頁可能會出事，所以要設這個東東。
格式就純提供jpg跟png，當然使用者如果要輸入其他格式也不是不行，只是我不知道有什麼其他跟圖片有關的格式。

------

```
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
```

後面這邊就是很正常的爬蟲動作，我自己測試是都正常，但某些網頁，比如說IG，個人的網頁剛點進去的時候，貼文的照片在被點開之前其實都不會顯示在source code裡面，所以抓不到。而且有些網頁會防爬蟲，這時候可能就要去設delay的時間來避免被抓等等。沒有打算花太多時間在這個東西上面，就這樣吧。
