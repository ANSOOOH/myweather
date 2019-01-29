# Requests Import
import requests
 
# Api 및 Token 정보
API_HOST = 'https://notify-api.line.me'
headers = {'Authorization': 'Bearer 1fNgw0MPePRMlJgkNZ2UHyq7iID1sjuqE0RcGDyTA7U'}
data = {}
 
# get & post 호출 정의
def req(path, query, method, data={}):
    url = API_HOST + path
 
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)
 
    if method == 'GET':
        return requests.get(url, headers=headers)
    else:
        return requests.post(url, headers=headers, data=data)
 
# 메신저로 보낼 메세지 내용
message = "파이썬 강의 첫번째, Notify로 알람보내기 테스트입니다."
imageThumbnail='https://tistory4.daumcdn.net/tistory/2535982/attach/f4524efd9ad4468b8fe19c0603b4c855'
imageFullsize='https://tistory4.daumcdn.net/tistory/2535982/attach/f4524efd9ad4468b8fe19c0603b4c855'
 
# parameter 값 및 호출 실행
params = {"message": message, "stickerId":106, "stickerPackageId":1}
# params = {"message": message, "imageThumbnail" :imageThumbnail, "imageFullsize" : imageFullsize}
resp = req('/api/notify', '', 'POST', params)
 
# Response
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
print("response body:\n%s" % resp.text)