#specialized for myself

from bs4 import BeautifulSoup
import requests
import os
 
#input_image = input("words:")
 
response = requests.get(f"https://telegra.ph/AS-I-AM--%E3%81%82%E3%82%8B%E3%81%8C%E3%81%BE%E3%81%BE%E3%81%AB--%E8%91%B5%E3%81%A4%E3%81%8B%E3%81%95%E5%86%99%E7%9C%9F%E9%9B%86-109P-02-18?fbclid=IwAR3Tx3nInGF8VGUx931s5YcFWWSaGb-BSf3l5LFeTbZHclgVSafxrcoNRX8")
soup = BeautifulSoup(response.text, "lxml")
 
results = soup.find_all("img", limit = 5)
 
image_links = [result.get("src") for result in results]  # 取得圖片來源連結
 
for index, link in enumerate(image_links):
    
    if not os.path.exists("images"):
        os.mkdir("images")  # 建立資料夾
 
    img = requests.get("https://telegra.ph" + link)  # 下載圖片
 
    with open("images\\" + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)  # 寫入圖片的二進位碼