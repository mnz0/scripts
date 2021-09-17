import os 
from shutil import copyfile
from pathlib import Path


if Path("D:\Program Files (x86)\Steam\steamapps\common\Rocksmith2014\dlc\CDLC").exists(): #laptop
    rocksmith_cdlc_path = Path("D:\Program Files (x86)\Steam\steamapps\common\Rocksmith2014\dlc\CDLC") 
else: print("You at PC")

if Path("E:\Games\Steam\steamapps\common\Rocksmith2014\dlc\CDLC").exists():
    rocksmith_cdlc_path=Path("E:\Games\Steam\steamapps\common\Rocksmith2014\dlc\CDLC") #PC
else: print("Alone on the kithen")
   

curent_dir = Path(os.getcwd())

dirRS_list = os.listdir(rocksmith_cdlc_path)
dirYD_list = os.listdir(os.getcwd())
new_entry = []

dif_list = set(list(dirYD_list)) - set(list(dirRS_list)) #get new files
list(dif_list)

for YD_file in dif_list:
    if YD_file not in dirRS_list and YD_file.endswith(".psarc"): # if file in YandexDisk folder not present in Rockcmith dir
        new_entry.append(YD_file) 

for f in new_entry:
    copyfile(Path(curent_dir, f), Path(rocksmith_cdlc_path, f)) 
    print(f + " was copy")
print("Copy " + str(len(new_entry)) + " songs. " +  "Now in you guitar lib " + str(len(dirYD_list)) + " entries!")
