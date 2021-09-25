import os
import subprocess
import shutil
import datetime
from pathlib import Path

FOLDERS_PATTERN = ['SRC', 'RENDER','RESULT']
RESULT_PATTERN = ['DPX','TIF','DAILIES','JPEG']
PROJECT_PATH = Path("C:\prog\tmp")
FTP_PROJECT_PATH = Path("C:\prog\tmp\ftp")

def last_version_parse():
    pass

def copy_dailies_to_ftp():
    pass

def copy_dpx_to_ftp(src, ftp_dest):
    Path
    shutil.copy(src,ftp_dest)

def copy_matte_to_ftp():
    pass

def write_report():
    pass

def get_date():
    today = datetime.date.today()
    return today.strftime("%Y%m%d")
    
print(RESULT_PATTERN[2])