import requests
from json import JSONDecoder
import time

http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "your key"
secret = "your secret"

filepath = r"gaoyuanyuan.jpg"

#API说明二进制文件，需要用 post multipart/form-data 的方式上传
data = {"api_key": key, "api_secret": secret, "return_landmark": "1" , "return_attributes":"gender,ethnicity,age,smiling,emotion,beauty"}


files = {"image_file": open(filepath, "rb")}
response = requests.post(http_url, data=data ,files=files)


req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print("本次请求ID：" ,req_dict["request_id"])
print("---------------------------------------------------")
print("姓名：高圆圆")
print("年龄：",req_dict["faces"][0]["attributes"]["age"]["value"])
print("性别：",req_dict["faces"][0]["attributes"]["gender"]["value"])
print("人种：",req_dict["faces"][0]["attributes"]["ethnicity"]["value"])
print("男性认为的此人脸颜值分数：",req_dict["faces"][0]["attributes"]["beauty"]["male_score"])
print("女性认为的此人脸颜值分数：",req_dict["faces"][0]["attributes"]["beauty"]["female_score"])
print("面部表情指数：",req_dict["faces"][0]["attributes"]["emotion"])


#print(req_dict["faces"][0]["attributes"])








