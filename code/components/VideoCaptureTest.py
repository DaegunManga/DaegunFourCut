import cv2 
import numpy as np
def StartCapturing(n) :
    cap = cv2.VideoCapture(1)

    ret, frame = cap.read() # 두 개의 값을 반환하므로 두 변수 지정
    y, x = 1862/4.1, 1313/4.1
    
    print(frame.shape[:2])
    # 비디오 매 프레임 처리
    while True: # 무한 루프
        ret, frame = cap.read() # 두 개의 값을 반환하므로 두 변수 지정

        if not ret: # 새로운 프레임을 못받아 왔을 때 braek
            break
        
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도 회전
        frame = cv2.flip(frame, 1) 

        m_big = np.float32([[2, 0, 0],
                     [0, 2, 0]]) 
        frame = cv2.warpAffine(frame, m_big, (960, 1280), None, cv2.INTER_CUBIC)

        cv2.imshow('frame', frame[int(525-y) : int(525+y), int(480-x) : int(480+x)])


        # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
        if cv2.waitKey(10) == 27:
            break
        if cv2.waitKeyEx(1) == 2555904 :
            cv2.imwrite(f'../src/Picture{n}.jpg', frame[int(525-y) : int(525+y), int(480-x) : int(480+x)])
            break            

    cap.release() # 사용한 자원 해제
    cv2.destroyAllWindows()

