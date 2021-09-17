from pathlib import Path
#import subprocess #for "ls -l >> list(today).txt"
import datetime
import os # for os.listdir


def get_today_date():
    today = datetime.date.today
    return today().strftime("%Y%m%d")


def get_folders_list(path):
    folders_list = os.listdir(path)
    return folders_list
    

def write_report_file(dirs_list):
    with open(today_date_str + ".txt", "a+") as f:
        for folder in dirs_list:
            f.write(folder + "\n")


upload_folder = Path("C:\Program Files")
today_date_str = get_today_date()
folders_list = get_folders_list(upload_folder)


write_report_file(folders_list)
