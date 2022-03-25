import pyautogui
from time import sleep
import shutil
from mytoken import myToken
from function import ch_rw, post_message, download_dir_call, dir_size, week_count, last_day, toast, day_folder_return
import datetime
import os

start_day = input("다운로드 시작 날짜를 입력하세요 : ").split(" ")
start_day = map(int, start_day)
disk = 'e:/'
desktop = 0

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def macro():
    day = start_day
    today = datetime.datetime(*day)
    ch = ch_rw()
    day_folder = day_folder_return(today)
    dir = download_dir_call()
    before_size = dir_size(dir + f'/{day_folder}')
    print("=================================================================")
    print(f'다운로드 시작 날짜 : {today.year}/{today.month}/{today.day}')
    print(f"채널 : {ch}")
    print("=====매크로 시작=====")
    while 1:
        sleep(10)
        day_folder = day_folder_return(today)
        after_size = dir_size(download_dir_call()+f'/{day_folder}')
        now = datetime.datetime.now()
        print(f"{now.month}/{now.day}-{now.hour}:{now.minute}:{now.second} - 실행중...")

        # if desktop == 1 and not pyautogui.locateOnScreen('./img/hims.png'):
        #     post_message(myToken, f"{ch}ch", 'hims 프로그램 꺼짐')
        #     print("hims프로그램이 꺼져서 매크로가 종료됨")
        #     break

        if before_size == after_size:
            print("========download finish========")

            toast.show()
            sleep(5)

            # if not pyautogui.locateOnScreen('./cancel.png'):
            #     desktop = 0

            pyautogui.hotkey('winleft', 'tab')
            sleep(1)
            desktop1 = pyautogui.locateOnScreen('./img/desktop1.png')
            if not pyautogui.locateOnScreen('./img/desktop1.png'):
                pyautogui.hotkey('winleft', 'tab')
            else:
                pyautogui.click(desktop1[0] + 30, desktop1[1] + 50, duration=1)

            total, used, free = shutil.disk_usage(disk)
            if free < 89120571392:
                post_message(myToken, f"{ch}ch", f'용량이 83기가보다 작아서 다운로드 중지')
                break

            pyautogui.click(pyautogui.locateOnScreen('./img/cancel.png'))

            if today.day == last_day(today).day:
                pyautogui.click("./img/month_change.png", duration=1)

            post_message(myToken, f"{ch}ch", f"{ch}ch {today.year}/{today.month}/{today.day} 다운로드 완료")

            today = today + datetime.timedelta(days=1)

            weekday_position = pyautogui.locateOnScreen(f'./img/{weekday[today.weekday()]}.png')

            pyautogui.moveTo(weekday_position, duration=0.1)
            pyautogui.click(weekday_position[0] + 10, weekday_position[1] + 36 + (26 * (week_count(today) - 1)), duration=1)

            pyautogui.click(pyautogui.locateOnScreen('./img/search.png'), duration=1)

            pyautogui.moveTo(pyautogui.locateOnScreen('./img/window1.png'), duration=1)
            pyautogui.click(pyautogui.locateOnScreen('./img/download_button.png'), duration=1)
            sleep(2)
            pyautogui.click(pyautogui.locateOnScreen('./img/download_all_check.png'), duration=1)

            if (used / total) * 100 > 70:
                post_message(myToken, f"{ch}ch", f"디스크 사용량이 70퍼센트를 넘었습니다.")

            pyautogui.click(pyautogui.locateOnScreen('./img/download_start.png'), duration=1)

        before_size = after_size

macro()
