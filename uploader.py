from errno import ENETUNREACH
import os
import shutil
import datetime
from pathlib import Path
import re
import json
from traceback import print_tb
import glob

FOLDERS_PATTERN = ['SRC', 'RENDER','RESULT']
RESULT_PATTERN = ['DPX','TIF','DAILIES','JPEG']
PROJECT_PATH = Path(r"C:\prog\ref\TEST_PROJ\SHOTS") 
FTP_PROJECT_PATH = Path(r"C:\prog\ref\poj1\ftp") #add row


def get_shot_list(): 
    is_episode = False
    shot_list = []
    episode_list = []
    shot_db = []
    os.chdir(PROJECT_PATH)
    folders_list = os.listdir(PROJECT_PATH)
    episode_size = 0


    for episode_index, ep_folder in enumerate(folders_list): #get index from list dirs

        if("SC" in ep_folder or "EP" in ep_folder or "S" or "SE" in ep_folder):
            episode_list.append(PROJECT_PATH.joinpath(ep_folder))

    episode_size = len(episode_list)

    while(episode_size != 0):

 
        os.chdir(episode_list[episode_size-1])
        print(Path.cwd())
        episode_size -= 1
        scan_shot_list = [shot for shot in os.listdir(cur_cwd)] # generator for light  list shots 
        glob.glob("..")# up to ep list

    for shot_index,shot in enumerate(episode_list):
        
            shot_list.append(os.listdir(shot))

               #TODO Dive into shot and append shot name to global path
            # os.chdir(prew_cwd)
    

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