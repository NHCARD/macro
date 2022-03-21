import pyautogui
import shutil
from time import sleep
import datetime
import shutil
from mytoken import myToken
from function import ch_rw, post_message, download_dir_call, dir_size, week_count, last_day, toast, day_folder_return

start_day = input("다운로드 시작 날짜를 입력하세요 : ").split(" ")
start_day = map(int, start_day)

disk = 'c:/'

weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def macro():
    day = start_day
    today = datetime.datetime(*day)
    ch = ch_rw()
    print("=================================================================")
    print(f'다운로드 시작 날짜 : {today.year}/{today.month}/{today.day}')
    print(f"채널 : {ch}")
    print("=====매크로 시작=====")
    while 1:
        sleep(5)
        now = datetime.datetime.now()
        print(f"{now.month}/{now.day}-{now.hour}:{now.minute} - 실행중...")

        if not pyautogui.locateOnScreen('./img/hims.png'):
            post_message(myToken, f"test", 'hims 프로그램 꺼짐')
            print("hims프로그램이 꺼져서 매크로가 종료됨")
            break

        if not pyautogui.locateOnScreen('./img/download.png'):
            print("========download finish========")
            pyautogui.click(pyautogui.locateOnScreen('./img/cancel.png'))

            if today.day == last_day(today).day:
                pyautogui.click("./img/month_change.png", duration=1)

            post_message(myToken, f"test", f"{ch}ch {today.year}/{today.month}/{today.day} 다운로드 완료")

            today = today + datetime.timedelta(days=1)

            weekday_position = pyautogui.locateOnScreen(f'./img/{weekday[today.weekday()]}.png')

            pyautogui.moveTo(weekday_position, duration=0.1)
            pyautogui.click(weekday_position[0] + 10, weekday_position[1] + 36 + (26 * (week_count(today) - 1)), duration=1)

            pyautogui.click(pyautogui.locateOnScreen('./img/search.png'), duration=1)

            pyautogui.moveTo(pyautogui.locateOnScreen('./img/window1.png'), duration=1)
            pyautogui.click(pyautogui.locateOnScreen('./img/download_button.png'), duration=1)
            sleep(2)
            pyautogui.click(pyautogui.locateOnScreen('./img/download_all_check.png'), duration=1)

            total, used, free = shutil.disk_usage(disk)

            if (used / total) * 100 > 70:
                post_message(myToken, f"test", f"디스크 사용량이 70퍼센트를 넘었습니다.")

            if free < 89120571392:
                post_message(myToken, f"test", f'용량이 83기가보다 작아서 다운로드 중지')

            pyautogui.click(pyautogui.locateOnScreen('./img/download_start.png'), duration=1)
            print(today)

macro()
