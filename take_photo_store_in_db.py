import cv2
import os
import buttonpython.faces_train as train_new_model

def takephoto():
    uid =0
    uid = input("Please enter user name")

    cam = cv2.VideoCapture(0)

    #cv2.namedWindow("Say Cheese")


    img_counter = 0
    num = 5
    val = 0
    newpath = "C:\\Users\\Admin\\buttonpython\\buttonpython\\images\\"+str(uid)
    if not os.path.exists(newpath):
        os.mkdir("C:\\Users\\Admin\\buttonpython\\buttonpython\\images\\"+str(uid))

    path = 'C:\\Users\\Admin\\buttonpython\\buttonpython\\images\\'+str(uid)

    while True:
        #uid = input("Please enter user id")
        ret, frame = cam.read()
        cv2.imshow("Say Cheese-Normal-Smile", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            while(img_counter<1):
                img_name = "User_{}.png".format(uid)
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                            if os.path.isfile(img_name):
                                val += 1
                    
                img_name = "User.png"#+str(val)+str(uid)
                #else:
                    #img_name = "User_{}.png".format(uid)                
                cv2.imwrite(os.path.join(path , img_name), frame)
                print("{} written!".format(img_name))
                img_counter += 1
                break
            #val += 1
            break
    print(img_name)
    cam.release()

    cv2.destroyAllWindows()

    train_new_model.trainit()
