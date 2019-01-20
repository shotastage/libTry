import os
import shutil



def preapre_cache_directory():
    home = os.environ['HOME']

    os.chdir(home)
