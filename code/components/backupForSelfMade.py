import os
from datetime import datetime
import shutil

# API 연결 및 사전정보 입력
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload



def StartBackUp () :
    today = datetime.today()
    filename = str(today.year) +'.' + str(today.month) +'.' + str(today.day) +'.' + str(today.hour) +'.' + str(today.minute) +'.' + str(today.second)
    os.mkdir('./backup/'+filename)
    os.mkdir('./backup/'+filename+'/images')

    from_file_path = []
    to_file_path = './backup/'+filename+'/images' # 복사 위치 및 파일 이름 지정

    for n in range (8) :
        from_file_path.append('./src/Picture'+str(n)+'.jpg')

    for file_path in from_file_path :
        shutil.copy(file_path, to_file_path) 

    shutil.copy('./src/result.png', './backup/'+filename)

    # api 연결 및 사전정보 입력
    SCOPES = ['https://www.googleapis.com/auth/drive.metadata', 
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive']
    from oauth2client import file, client, tools
    store = file.Storage('./env/storage.json')
    creds = store.get()
        
    # 권한 인증 창. 제일 처음만 창이 띄워짐
    try :
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    if not creds or creds.invalid:
        print('make new cred')
        flow = client.flow_from_clientsecrets('./env/client_secret_drive.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) if flags else tools.run_flow(flow, store)
        
    service = build('drive','v3',credentials=creds)
        
    # 업로드 할 파일
    file_paths = "./src/result.png"
    
    filename = str(today.year) +'-' + str(today.month) +'-' + str(today.day) +'-' + str(today.hour) +'-' + str(today.minute) +'-' + str(today.second)
    
    # 업로드할 파일 정보 정의
    # parents: 업로드할 구글 드라이브 위치의 url 마지막 ID
    file_metadata = {
    "name": f"{filename}.png",
    "parents": ["1E1yVYiTDMtA1A1j9JKu_JK78WJWkFLCT"]}
    # 파일 업로드
    media = MediaFileUpload(file_paths, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

