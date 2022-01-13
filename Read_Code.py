import cv2
from pyzbar.pyzbar import decode
import json
import boto3

# method to decode the barcode.
# This will read the barcode image from local folder and will decode the barcode
img = cv2.imread('websiteQRCode_noFrame.png')
decoded_msg=decode(img)
dict_of_decoded_msg={"data":[],"type":[],"rect":[],"polygon":[]}
for x in decoded_msg:
    data_val = x.data.decode('utf-8')
    type = x.type
    rect = x.rect
    polygon = x.polygon
dict_of_decoded_msg["data"].append(data_val)
dict_of_decoded_msg["type"].append(type)
dict_of_decoded_msg["rect"].append(rect)
dict_of_decoded_msg["polygon"].append(polygon)
print(dict_of_decoded_msg)
json_string=json.dumps(dict_of_decoded_msg)
print(json_string)










