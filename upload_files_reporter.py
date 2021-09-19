from pathlib import Path
#import subprocess #for "ls -l >> list(today).txt"
import datetime
import os # for os.listdir

upload_folder = Path("D:\Distr")   #Temporart. Path will set in Main func

def get_today_date():
    today = datetime.date.today
    return today().strftime("%Y%m%d")

today_date_str = get_today_date()

def get_folders_list(path):
    folders_list = os.listdir(path)
    return folders_list
    

def write_report_file(dirs_list):
    entries_count = 0
    with open(today_date_str + ".txt", "a+") as f:
        for folder in dirs_list:
            entries_count +=1 
            f.write(str(entries_count) + ". " +  folder + "\n")

def main(path): 
    if Path(path).exists:
        print("Path exist...")
        folders = get_folders_list(path)
        write_report_file(folders)
    else:
        print("Path is not exitst...")

main(upload_folder)