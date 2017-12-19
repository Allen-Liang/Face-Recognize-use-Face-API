import requests
from json import JSONDecoder


#API账号相关信息，自己在自己的开发者中心查
http_url='https://api-cn.faceplusplus.com/facepp/v3/compare'
key = "your key"
secret = "your secret"

#需要compare本地图片路径
image1 = r"dahan.jpg"
image2 = r"minguo.jpg"

#API说明二进制文件，需要用 post multipart/form-data 的方式上传
data = {"api_key": key, "api_secret": secret, "return_landmark": "2"}
files = {"image_file1": open(image1, "rb"),"image_file2": open(image2, "rb")}


response = requests.post(http_url, data=data, files=files)


req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)


#输出响应的所有信息
#print(req_dict)
#输出两张照片的置信度0-100之间，数值越大说明两张脸越像
print("两张照片的置信度0-100之间，数值越大说明两张脸越像")
print("___________________________________________________")
print("大韩和民国之间的置信度为：",req_dict["confidence"])






