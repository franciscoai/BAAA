#!/usr/bin/env python3
import os
import sys
#import hunspell
from termcolor import colored
import numpy as np
import PyPDF2
import pandas as pd
from pylatexenc.latexencode import unicode_to_latex
from chardet.universaldetector import UniversalDetector
import difflib
import re
import checkCRAAA

"""

Script to check the editorial style of the CRAAA for all the .tex files in the input dir.

Packages: See README

Usage: python3 checkCRAAA_dir.py /absolute/path/to/dir

Changes log:
-20201019: First version - - franciscoaiglesias@gmail.com 

"""
#CONSTANTS

if __name__ == '__main__':

    dirn = sys.argv[1]
    fl=os.listdir(dirn)  # file lsit 
    
    for f in fl:
      if f.endswith('.tex'):
        os.system('python3 checkCRAAA.py '+dirn+'/'+f)
    
