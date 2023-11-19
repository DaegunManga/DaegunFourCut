import cv2 
import numpy as np
def StartCrop (n_List:list, case:int) :
    test=[]
    if case == 1 : 
        for n in n_List :
            test.append(cv2.imread('../src/Picture'+str(n)+'.jpg', cv2.IMREAD_COLOR))
        test0 = test[0]
        test1 = test[1]
        test2 = test[2]
        test3 = test[3]
        back = cv2.imread('../utils/background.png', cv2.IMREAD_COLOR)

        imsize = [1340, 1894]

        test0 = cv2.resize(test0, dsize=(int(imsize[0]), int(imsize[1])))
        test1 = cv2.resize(test1, dsize=(int(imsize[0]), int(imsize[1])))
        test2 = cv2.resize(test2, dsize=(int(imsize[0]), int(imsize[1])))
        test3 = cv2.resize(test3, dsize=(int(imsize[0]), int(imsize[1])))

        h, w = test0.shape[:2]   
        #crop = back[970:h+970, 125:w+125]
        #cv2.copyTo(test, mask, crop)


        back[138:h+138, 208:w+208] = test0
        back[138:h+138, 1610:w+1610] = test1
        back[2082:h+2082, 208:w+208] = test2
        back[2082:h+2082, 1610:w+1610] = test3

        h, w = back.shape[:2]
        resize_img = cv2.resize(back, dsize=(int(w/5), int(h/5)))

        cv2.imwrite('../src/result.png', back[:, :-40])
        cv2.waitKey()

        #import backup
    elif case == 2 : 
        for n in n_List :
            test.append(cv2.imread('../src/Picture'+str(n)+'.jpg', cv2.IMREAD_ANYCOLOR))
        test0 = test[0]
        test1 = test[1]
        test2 = test[2]
        test3 = test[3]
        back = cv2.imread('../utils/background.png')

        imsize = [1340, 1894]

        test0 = cv2.resize(test0, dsize=(int(imsize[0]), int(imsize[1])))
        test1 = cv2.resize(test1, dsize=(int(imsize[0]), int(imsize[1])))
        test2 = cv2.resize(test2, dsize=(int(imsize[0]), int(imsize[1])))
        test3 = cv2.resize(test3, dsize=(int(imsize[0]), int(imsize[1])))

        Daegun_character = cv2.imread('../utils/Daegun_char.png' ,cv2.IMREAD_UNCHANGED)

        h, w = test0.shape[:2]   
    

        back[138:h+138, 208:w+208] = test0
        back[138:h+138, 1610:w+1610] = test1
        back[2082:h+2082, 208:w+208] = test2
        back[2082:h+2082, 1610:w+1610] = test3


        _, mask = cv2.threshold(Daegun_character[:, :, 3], 1, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img_fg = cv2.cvtColor(Daegun_character, cv2.COLOR_BGRA2BGR)
        h, w = img_fg.shape[:2]
        roi = back[0:h, 100:w+100]

        masked_fg = cv2.bitwise_and(img_fg, img_fg, mask=mask) 
        masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)    

        added = masked_fg + masked_bg
        back[0:h, 100:w+100] = added

        cv2.imwrite('../src/result.png', back[:, :-40])
        cv2.waitKey()

        #import backup
    
    elif case == 3 :
        for n in n_List :
            test.append(cv2.imread('../src/Picture'+str(n)+'.jpg', cv2.IMREAD_COLOR))
        test0 = test[0]
        test1 = test[1]
        test2 = test[2]
        test3 = test[3]
        test4 = test[4]
        test5 = test[5]
        back = cv2.imread('../utils/background2.png', cv2.IMREAD_COLOR)

        imsize = [637, 900]

        test0 = cv2.resize(test0, dsize=(int(imsize[0]), int(imsize[1])))
        test1 = cv2.resize(test1, dsize=(int(imsize[0]), int(imsize[1])))
        test2 = cv2.resize(test2, dsize=(int(imsize[0]), int(imsize[1])))
        test3 = cv2.resize(test3, dsize=(int(imsize[0]), int(imsize[1])))
        test4 = cv2.resize(test4, dsize=(int(imsize[0]), int(imsize[1])))
        test5 = cv2.resize(test5, dsize=(int(imsize[0]), int(imsize[1])))

        h, w = test0.shape[:2]   
        #820 - 183
        #cv2.copyTo(test, mask, crop)
        # 183 107

        back[107:h+107, 183:w+183] = test0
        back[107:h+107, 923:w+923] = test1
        back[107:h+107, 1664:w+1664] = test2
        back[1080:h+1080, 183:w+183] = test3
        back[1080:h+1080, 923:w+923] = test4
        back[1080:h+1080, 1664:w+1664] = test5

        h, w = back.shape[:2]

        cv2.imwrite('../src/result.png', back[:, :])
        cv2.waitKey()
    else :
        for n in n_List :
            test.append(cv2.imread('../src/Picture'+str(n)+'.jpg', cv2.IMREAD_COLOR))
        test0 = test[0]
        test1 = test[1]
        test2 = test[2]
        test3 = test[3]
        test4 = test[4]
        test5 = test[5]
        back = cv2.imread('../utils/background1.png', cv2.IMREAD_COLOR)

        imsize = [487, 696]

        test0 = cv2.resize(test0, dsize=(int(imsize[0]), int(imsize[1])))
        test1 = cv2.resize(test1, dsize=(int(imsize[0]), int(imsize[1])))
        test2 = cv2.resize(test2, dsize=(int(imsize[0]), int(imsize[1])))
        test3 = cv2.resize(test3, dsize=(int(imsize[0]), int(imsize[1])))
        test4 = cv2.resize(test4, dsize=(int(imsize[0]), int(imsize[1])))
        test5 = cv2.resize(test5, dsize=(int(imsize[0]), int(imsize[1])))

        h, w = test0.shape[:2]   


        back[81:h+81, 141:w+141] = test0
        back[81:h+81, 712:w+712] = test1
        back[81:h+81, 1284:w+1284] = test2
        back[835:h+835, 141:w+141] = test3
        back[835:h+835, 712:w+712] = test4
        back[835:h+835, 1284:w+1284] = test5

        h, w = back.shape[:2]

        cv2.imwrite('../src/result.png', back[:-40, :])
        cv2.waitKey()



