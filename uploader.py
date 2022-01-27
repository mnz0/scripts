import os
import shutil
import datetime
from pathlib import Path
import re
import json

FOLDERS_PATTERN = ['SRC', 'RENDER','RESULT']
RESULT_PATTERN = ['DPX','TIF','DAILIES','JPEG']
PROJECT_PATH = Path(r"C:\prog\ref\TEST_PROJ\SHOTS") 
FTP_PROJECT_PATH = Path(r"C:\prog\ref\poj1\ftp") #add row


def get_shot_list(): 
    is_episode = False
    shot_list = []
    episode_list = []
    shot_db = []
    folders_list = os.listdir(PROJECT_PATH)
    for ep_folder in folders_list:
        if("SC" in ep_folder or "EP" in ep_folder or "S" in ep_folder):
            episode_list.append(PROJECT_PATH.joinpath(ep_folder))
    

    for i in episode_list:
        print(i)
    # return EP_list




def last_version_parse(path):
    os.chdir(Path(path))
    upper_version = "v000"
    folders = os.listdir(os.getcwd())
    versions_list = re.findall(r'v\d{3}',str(folders))
    return versions_list

def copy_dailies_to_ftp(d_src, ftp_dest):
    shutil.copy(d_src, ftp_dest + "/DAILIES")

def get_today_date():
    today = datetime.date.today()
    return today.strftime("%Y%m%d")

def get_status():
    os.chdir(Path.absolute)
    with open ("status.json", "r") as jfile:
        jfile.read
    json.loads(jsonData)
    pass
get_shot_list()
# for i in lst:
#     print(i)