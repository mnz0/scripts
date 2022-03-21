from up_func import *
 

PROJECT_PATH = Path(r"C:\prog\ref\TEST_PROJ\SHOTS") 
FTP_PROJECT_PATH = Path(r"C:\prog\ref\poj1\ftp") #add row

shot_list = get_shot_list(PROJECT_PATH)




for index, shot in enumerate(shot_list):
    print(str(index) + " " + str(shot))