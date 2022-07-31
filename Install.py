import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from Termux64 import data_base

    data_base()

elif bit == '32bit':

    from Termux import data_base

    data_base()
