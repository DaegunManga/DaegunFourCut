import qrcode
import cv2
import components.backup as bc

def StartMakeQR (url, type) :

    image_url = qrcode.make(url)
    image_url.save("../src/QR.png")
    if type == 1 or 2: 
        back = cv2.imread('../src/result.png', cv2.IMREAD_COLOR)
        QR = cv2.imread('../src/QR.png', cv2.IMREAD_COLOR)
        QR = cv2.resize(QR, dsize=(200, 200))

        h, w = QR.shape[:2]
        print(back.shape)
        back[4190:h+4190, 260:w+260] = QR # 2769 1950
        cv2.imwrite('../src/resultwithQR.png', back[:, :])

    elif type == 3 or 4 : 
        back = cv2.imread('../src/result.png', cv2.IMREAD_COLOR)
        QR = cv2.imread('../src/QR.png', cv2.IMREAD_COLOR)
        QR = cv2.resize(QR, dsize=(150, 150))

        h, w = QR.shape[:2]

        back[1935:h+1935, 2795:w+2795] = QR# 2769 1950
        cv2.imwrite('../src/resultwithQR.png', back[:, :])
    
    bc.StartBackUp()
