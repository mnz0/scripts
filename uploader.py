import os
# import subprocess
import shutil
import datetime
from pathlib import Path
from typing import OrderedDict
import re

FOLDERS_PATTERN = ['SRC', 'RENDER','RESULT']
RESULT_PATTERN = ['DPX','TIF','DAILIES','JPEG']
PROJECT_PATH = Path(r"C:\Program Files") #add row
FTP_PROJECT_PATH = Path(r"C:\prog\tmp\ftp") #add row


def get_folders_list(results_path):
    CWD = os.getcwd()
    
    return os.listdir(results_path)

def last_version_parse(path_to_folder):
    os.chdir(Path(path_to_folder))
    upper_version = "v000"
    folders = os.listdir(os.getcwd())
    versions_list = re.findall(r'v\d{3}',str(folders))
    list(num_list) = 0
    for num in versions_list:
        

    return versions_list

def copy_dailies_to_ftp(d_src, ftp_dest):
    pass

def copy_dpx_to_ftp(src, ftp_dest):
    ftp_dest =  Path(FTP_PROJECT_PATH).joinpath(RESULT_PATTERN[0])
    shutil.copy(src,ftp_dest)

def copy_matte_to_ftp(src, matte_dst):
    shutil.copy(src, matte_dst)

def write_report():
    pass

def get_date():
    today = datetime.date.today()
    return today.strftime("%Y%m%d")

# for f in (get_folders_list(PROJECT_PATH)):
#     print(f)


print(last_version_parse(FTP_PROJECT_PATH))