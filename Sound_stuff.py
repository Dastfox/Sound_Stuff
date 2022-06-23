

from msilib.schema import Shortcut
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from os import listdir
from os.path import isfile, join
from pathlib import Path
from glob import glob
import winshell
import os
from win32com.client import Dispatch
import os, winshell, win32com.client
from PIL import Image

import librosa as lr
import librosa.display
import IPython.display as ipd

from itertools import cycle

# Setting some appearance 
sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])


# setting music's base dir & file names dict
data_dir = './SoundFiles'
audio_files = glob(f'{data_dir}/*.wav')
dir_path = os.path.dirname(os.path.realpath(__file__))

# loading the music and saving the png

for i in range(len(audio_files)):
    
    ipd.Audio(audio_files[i])
    y, sr = lr.load(audio_files[i])
    tempo = librosa.beat.tempo(y=y, sr=sr)
    tempoR = '%.1f' % (tempo,)
    name = f'{Path(audio_files[i]).stem} {tempoR} bpm'
    if not os.path.exists(f'./Plots/{name}'):
        y_trimmed, _ = librosa.effects.trim(y, top_db=20)
        pd.Series(y_trimmed).plot(figsize=(15, 5),
                     lw=1,
                     title=name,
                     color=color_pal[1])
        plt.savefig("./Plots/"f'{name} WF.png')
        icon = ("./Plots/"f'{name} WF.png')
        path = ("Shortcuts/"f'{Path(audio_files[i]).stem}.lnk')
        shell = win32com.client.Dispatch("WScript.Shell")
        target = (f'{dir_path}/{audio_files[i]}')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.IconLocation = icon
        shortcut.save()
        print(audio_files[i])
        print(target)
        print(icon)
        
        
    

# to uncomment if seeing plot data is needed
# print(f'y: {y[:10]}')
# print(f'shape y: {y.shape}')
# print(f'sr: {sr}')



