from errno import ENETUNREACH
import os
import shutil
import datetime
from pathlib import Path
import re
import json
import Shot


FOLDERS_PATTERN = ['SRC', 'RENDER','RESULT']
RESULT_PATTERN = ['DPX','TIF','DAILIES','JPEG']
RULES_SUBFOLDER  = Path(r".rules")


def get_shot_list(PROJECT_PATH): 
    shot_list = []

    episode_list = []
    shot_db = []
    out_shot_db = []
    os.chdir(PROJECT_PATH)
    folders_list = os.listdir(PROJECT_PATH)
    serial_episode_pattern =["SC", "EP", "S", "SE", "SER"]

    for index, ep_folder in enumerate(folders_list): #get index from list dirs
        match_pattern = re.search(r"\S+\d+", ep_folder)  
        if(match_pattern):
            episode_list.append(PROJECT_PATH.joinpath(ep_folder))
            prew_cwd = Path.cwd()
            try:
                os.chdir(episode_list[index])
                shot_db.append(episode_list[index])
                cur_cwd = Path.cwd()
                scan_shot_list = [shot for shot in os.listdir(cur_cwd)]
                list(scan_shot_list)
                for shot in scan_shot_list:
                    out_shot_db.append(Path(Path.cwd().joinpath(shot)))
                os.chdir(r"..")
                # glob.glob("..") instead chdir? need test on Rulez
            except IOError as exp:
                raise IOError ("Can`t open folder " + str(cur_cwd)) from exp 
    return out_shot_db
    
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
