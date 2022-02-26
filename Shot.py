#Shot class file

import os
import glob
import json
from pathlib import Path

'''


'''
class Shot:
    
    def __init__(self, shot_name, shot_location, shot_status):
        self.shot_name = shot_name
        self.shot_location = shot_location
        self.shot_status = shot_status

    
        