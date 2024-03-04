import cryptocode
import pyautogui
from pyautogui import locateOnScreen
from time import sleep
import datetime
import shutil
# from function import ch_rw, post_message, download_dir_call, dir_size, week_count, last_day, toast, day_folder_return
from function import post_message
import cv2

token = "6e/uZyTVB9NWybo8t19tTu7qoaE79gG4LICXkGyYkN2DhRRWMDS+aZhtKKnsBIbahWQdyRULoqVO*9vtRe893ZpantrRQgfMB7A==*VjXqcR3GDbV/Ip76eH1kpw==*GKu1W/kFzpi734ifhO9BKQ=="

decode_token = cryptocode.decrypt(token, "wow")
def notification():
    print("Run!")
    while(1):
        sleep(120)
        now = datetime.datetime.now()
        print(f"{now.month}/{now.day}-{now.hour}:{now.minute}:{now.second} - Running...")
        if not locateOnScreen('./img/download_2023.png'):
            post_message(decode_token, f"download", 'download complete')
            break


notification()
