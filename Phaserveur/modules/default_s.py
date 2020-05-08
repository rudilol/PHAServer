import sys
import os
from time import sleep
from core.system import *
from modules.php import *
from modules.pyweb import *

def default_s():
  if os.path.exists(bpath+"php"):
    php()
  else:
    pyweb()