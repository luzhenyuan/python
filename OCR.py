#encoding:utf-8
from aip import AipOcr
import sys, os
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf-8')
class Ocr(object):

    def __init__(self):

        """ 你的 APPID AK SK """
        APP_ID = '10338048'
        API_KEY = 'HFB4G6hNFIC1vBF09fwrCujI'
        SECRET_KEY = '7M4NtLAgHoLKF7xKkKQTukqxapyORbry'
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, image):

        """ 读取图片 """
        with open(image, 'rb') as fp:
            return fp.read()

    def OcrApi(self, fd):

        """ 调用通用文字识别, 图片参数为本地图片 """
        data = self.client.basicAccurate(fd)
        self.data1 =data['words_result'][9]['words']+\
            '     '+data['words_result'][11]['words']+\
            data['words_result'][10]['words'] +\
            '     '+data['words_result'][12]['words'] +\
            '     '+data['words_result'][15]['words']
    # 数据存储
    def SaveDataToCSV(self):
        f = open('test.txt', 'a')
        f.write(self.data1+'\n')
        f.close()

    def ima(self):
        os.popen('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
        os.popen('adb pull /sdcard/screenshot.png ./images/1.png')
        # 读取图像
        im = Image.open("./images/1.png")
        # 指定逆时针旋转的角度
        im = im.resize((1080, 1920))
        im_rotate = im.transpose(Image.ROTATE_90)
        im_rotate.save('./images/1.png')
        return
    def run(self):
        self.ima()
        data = self.get_file_content('images/1.png')
        self.OcrApi(data)
        self.SaveDataToCSV()