import requests


#보내고자하는 파일을 'rb'(바이너리 리드)방식 열고
files = open('./src/result.png', 'rb')

# 파이썬 딕셔너리 형식으로 file 설정
upload = {'photo':files}


# request.post방식으로 파일전송.
res = requests.post('http://photo.dgmanga.kr/upload', files = upload)