import requests
import os
import datetime
from winotify import Notification

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                            headers={"Authorization": "Bearer " + token},
                            data={"channel": channel, "text": text}
                            )

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

def download_dir_call():
    file_list = os.listdir('./')

    if 'download_dir.txt' in file_list:
        f = open('./download_dir.txt', 'r')
        dir = f.read()
        f.close()
        return dir
    elif 'download_dir.txt' not in file_list:
        f = open('./download_dir.txt', 'w')
        dir = str(input("다운로드 경로를 입력하세요. 최초 1회만 입력받습니다 : "))
        f.write(dir)
        f.close()
        return dir

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

def dir_size(folder):
    size = 0
    file_list = os.listdir(folder)
    for i in file_list:
        size += os.path.getsize(folder + '/' + i)
    return size

def day_folder_return(day):
    if len(str(day.month)) == 1:
        month = '0'+ str(day.month)
    elif len(str(day.month)) == 2:
        month = day.month
    if len(str(day.day)) == 1:
        day_r = '0' + str(day.day)
    elif len(str(day.day)) == 2:
        day_r = day.day

    return str(day.year)+str(month)+str(day_r)

toast = Notification(icon=r"C:\Users\default.DESKTOP-A9BC2Q6\Desktop/test.png",
                     app_id="macro",
                     title="다운로드 완료",
                     msg="매크로 작동까지 마우스 멈춰!"
                     )
