

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from os import listdir
from os.path import isfile, join
from pathlib import Path
from glob import glob

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

# loading the music and saving the png

for i in range(len(audio_files)):
    
    ipd.Audio(audio_files[i])
    y, sr = lr.load(audio_files[i])
    tempo = librosa.beat.tempo(y=y, sr=sr)
    tempoR = '%G' % (tempo,)
    name = f'{Path(audio_files[i]).stem} {tempoR} bpm'
    y_trimmed, _ = librosa.effects.trim(y, top_db=20)
    pd.Series(y_trimmed).plot(figsize=(20, 5),
                  lw=1,
                  title=name,
                 color=color_pal[1])
    plt.savefig("./Plots/"f'{name} WF.png')

# to uncomment if seeing plot data is needed
# print(f'y: {y[:10]}')
# print(f'shape y: {y.shape}')
# print(f'sr: {sr}')



