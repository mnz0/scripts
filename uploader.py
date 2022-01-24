import os
import shutil
import datetime
from pathlib import Path
import re
import json
from this import d

FOLDERS_PATTERN = ['SRC', 'RENDER','RESULT']
RESULT_PATTERN = ['DPX','TIF','DAILIES','JPEG']
PROJECT_PATH = Path(r"C:\prog\ref\TEST_PROJ") 
FTP_PROJECT_PATH = Path(r"C:\prog\ref\poj1\ftp") #add row


def get_shot_list(path):

    return os.walk(path)

def last_version_parse(path):
    os.chdir(Path(path))
    upper_version = "v000"
    folders = os.listdir(os.getcwd())
    versions_list = re.findall(r'v\d{3}',str(folders))
    return versions_list
3
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


shot_list = get_shot_list(PROJECT_PATH)
for f in shot_list:
    print(f)