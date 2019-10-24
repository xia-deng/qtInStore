import os

import cv2

from pic_read import BaiduApi


class camera_driver(object):

    def __pic_dir__(self):
        print(os.path.abspath("../temp"))
        return os.path.abspath("../temp")

    def camera_open(self, path, type):
        camera = cv2.VideoCapture(0)
        img = path + os.sep + type + ".jpeg"
        print(img)
        if(os.path.exists(img)):
            os.remove(img)
        try:
            while os.path.exists(img) is False:
                ref, frame = camera.read()
                cv2.imshow("InStore", frame)
                key = cv2.waitKey(10);
                #按下空格键，拍摄并退出
                if key == 32:
                    cv2.imwrite(os.path.abspath(img), frame)
                    camera.release()
                    cv2.destroyAllWindows()
                    break
            return True
        except Exception as e:
            print("打开摄像头操作失败: %s" % e)
            return False


# cv2.waitKey()
# cv2.destroyAllWindows()
