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
import csv
 
"""

Script to check the editorial style of the CRAAA for all the .tex files in ipath that are in subdirs included in idlist.

Packages: See README

Usage: python3 checkCRAAA_dir.py /absolute/path/to/dir

Changes log:
-20201019: First version - - franciscoaiglesias@gmail.com 

"""
#INPUTS
ipath='/media/sf_onedrive_utn/work/my_editions/2021_vasquez_CRAA63/papers'
opath='/media/sf_onedrive_utn/work/my_editions/2021_vasquez_CRAA63/Fran'

#CONSTANTS
root='/media/sf_onedrive_utn/work/repository/BAAA/' #path to the BAAA repo
idlist='IDnumList.csv' # list with id numbers to process from ipath
compf=['baaa.cls','logoAAA.pdf'] # files required to compile, assumed to be in root/


if __name__ == '__main__':

    #reads id list
    idl=['0']#np.array([0])
    with open(idlist, newline='') as csvfile:
        spamreader = csv.reader(csvfile)#, delimiter=',')#, quotechar='|')
        for row in spamreader:
            #print(row)
            idl.append(row[0])#np.concatenate(idl,row)
    idl=idl[1:]
    #ipath = sys.argv[1]
    fl=sorted(os.listdir(ipath))  # subdir lsit 
    fl=[os.path.basename(d) for d in fl if os.path.basename(d) in idl]
    print(fl)
    print(len(fl))
    #creates odir
    if not os.path.exists(opath): 
        os.makedirs(opath)  

    #run edition script for the first .tex in each fl dir, after copying the dir to opath and filling it with compf 
    for i in range(len(fl)):
        val='r'
        f=fl[i]
        if not os.path.exists(opath+'/'+f):
            print('>>>>>>>>>>>>>>>>>Copying dir...'+opath+'/'+f)
            os.system('cp -R '+ipath+'/'+f+' '+opath+'/.')
            for cf in compf:
                os.system('cp -R '+root+'/'+cf+' '+opath+'/'+f+'/.')
            tex=[tf for tf in os.listdir(opath+'/'+f) if tf.endswith('.tex')]
        while val=='r':
            os.system('python3 checkCRAAA.py '+opath+'/'+f+'/'+f+'.tex')
            val=input('Press \'r\' to process the same file again, any key to continue with the next file.\n')
        #else:
        #    print('>>>>>>>>>>>>>>>>Skipping existing dir...'+opath+'/'+f)
        #    os.system('python3 checkCRAAA.py '+opath+'/'+f+'/'+f+'.tex')
