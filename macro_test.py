import pyautogui
import requests
import os
import shutil
from time import sleep
import datetime
import shutil

start_day = input("다운로드 시작 날짜를 입력하세요 : ").split(" ")
start_day = map(int, start_day)

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                            headers={"Authorization": "Bearer " + token},
                            data={"channel": channel, "text": text}
                            )
myToken = "xoxb-3111133345761-3122283163856-e7DMpoeAMrqCTJDgYQOX6Dxb"

def ch_rw():
    file_list = os.listdir("./")

    if "ch_info.txt" not in file_list:
        ch = int(input("채널을 입력해주세요. 최초 1회만 입력받습니다 : "))
        f = open('./ch_info.txt', 'w')
        f.write(str(ch))
        f.close()
        return ch

    elif "ch_info.txt" in file_list:
        f = open('./ch_info.txt', 'r')
        ch = f.read()
        f.close()
        return ch

disk = 'c:/'

def week_count(day):
    firstday = day.replace(day=1)
    if firstday.weekday() == 6:
        origin = firstday
    elif firstday.weekday() < 3:
        origin = firstday - datetime.timedelta(days=firstday.weekday() + 1)
    else:
        origin = firstday + datetime.timedelta(days=6 - firstday.weekday())
    return (day - origin).days // 7 + 1

def last_day(day):
    next_month = day.replace(day=1, month=day.month+1)
    return next_month - datetime.timedelta(days=1)


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
