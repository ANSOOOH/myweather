#라인으로 사진, 글, 스티커 보내기
import requests

#API 및 Token 정보

url = 'https://notify-api.line.me/api/notify'

token = {'Authorization' : 'Bearer 1fNgw0MPePRMlJgkNZ2UHyq7iID1sjuqE0RcGDyTA7U'}
#data = {}

#이모티콘스티커 및 이미지 라인으로 보내기
imageThumbnail = "https://pbs.twimg.com/media/Dsc_0erWsAEm7aF.jpg"
imageFullsize = "https://pbs.twimg.com/media/Dsc_0erWsAEm7aF.jpg"
message = "새 글이 올라왔습니다."
# parameter = {"message": message}
parameter = {"message": message, "stickerId":106, "stickerPackageId":1}
# parameter = {"message": message, "imageThumbnail":imageThumbnail ,"imageFullsize":imageFullsize}


#Response
response = requests.post(
    url, headers = token, data = parameter
)
print(response.text)