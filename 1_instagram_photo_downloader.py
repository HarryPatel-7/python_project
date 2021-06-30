# METHOD 1 

import requests
import os
import json
import shutil


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

INSTA_URL = "https://www.instagram.com/"
USER_ID = "harry_3401"

TAIL = "/?__a=1"

URL = INSTA_URL + USER_ID + TAIL

response = requests.get(URL, headers=header).json()

#print("\n\n Downloading.........    \n\n")
#print("\n Download Complete ......... \n")


hd_image_location = r["graphql"]["user"]["profile_pic_url_hd"]
hd_image_response = requests.get(hd_image_location, stream=True)

with open(USER_ID+".jpg", "wb") as out_file:
    shutil.copyfileobj(hd_image_response.raw, out_file)