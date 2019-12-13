import requests

mp4_url = "https://video.pearvideo.com/mp4/short/20190926/cont-1605282-14426621-hd.mp4"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}

response = requests.get(url=mp4_url,headers=headers)

f = open("1.mp4",mode='wb')

f.write(response.content)

f.close()
