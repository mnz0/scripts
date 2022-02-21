#Shot class file

from msilib.schema import Class
import pathlib
import os
import glob

class Shot:

    def __init__(self, shot_name, shot_location):
        self.shot_name = shot_name
        self.shot_location = shot_location
        